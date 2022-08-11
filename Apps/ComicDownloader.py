import Apps.ComicDownloaderCore.Core as Core
import requests
from Websites.Link import Link
from Utilities.ProgressBar import progressbar
from Utilities.Utilities import repeater, create_folder_in_path


@repeater
def select_site():
    sites_name = ""

    for i, value in enumerate(Core.WEBSITES):
        sites_name += f"\n{i+1}.- {value.name}"

    print(f"\nEnter the number of the website where download the comic: {sites_name} \n")
    site = input("-- ")
    
    if site.strip().isdigit():
        site = int(site)

        website_lenght = len(Core.WEBSITES) - 1
        site = website_lenght if site > website_lenght else site - 1

        print(f"\nYou are searching comics in {Core.WEBSITES[site].name}.")
    
    else:
        site = None
        print("\nThat isn't a number. Try Again.")

    return site


@repeater
def select_comic(comics_link):
    c_link = None

    not_found = Link()
    not_found.tag = "** The comic you search is not in the list. **"
    not_found.url = ""
    comics_link.append(not_found)

    comics_name = ""
    for i, link in enumerate(comics_link):
        comics_name += f"\n{i+1}.- {link.tag}"

    print(f"\nEnter the number of the comic you choose: {comics_name} \n")

    comic_num = input("-- ")
    
    if comic_num.strip().isdigit():
        comic_num = int(comic_num)
        
        comics_lenght = len(comics_link) - 1
        comic_num = comics_lenght if comic_num > comics_lenght else comic_num - 1

        c_link = comics_link[comic_num]
    
    else:
        print("\nThat isn't a number. Try Again.")

    return c_link


@repeater
def search_comic(site):
    comic_link = None
    
    title = input("\nEnter the title of the comic:- ")
    comics = Core.get_all_comics_in_website(site, title)

    if not len(comics) > 0:
        print("\nNo comic found. Try again.")

    elif len(comics) == 1:
        comic_link = comics[0]
        print(f"\nOnly one comic match: {comic_link.tag}")
    
    else:
        comic_link = select_comic(comics)
        print(f"\nYou choose: {comic_link.tag}.")

    return comic_link


@repeater
def select_one_issue(issues_link):
    comic_num = input("\nSelect the number of the issue you want to download:- ")

    if not comic_num.strip().isdigit():
        print("\nThat isn't a number. Try again.")
        issues_link = None
    else:
        comic_num = int(comic_num) - 1
        issues_link = issues_link[comic_num:comic_num + 1]

    return issues_link


@repeater
def select_range_of_issues(issues_link):

    start = input("\nSelect the number of the issue from to start download:- ")
    end = input("Select the number of the last issue to download:- ")

    if not start.strip().isdigit():
        print("\nThat isn't a number. Try again.")
        issues_link = None

    elif not end.strip().isdigit():
        print("\nThat isn't a number. Try again.")
        issues_link = None
    
    else:
        start = int(start)
        end = int(end)
        
        issues_lenght = len(issues_link) - 1
        start = 0 if start - 1 < 0 else start - 1
        end = issues_lenght if end > issues_lenght else end

        issues_link = issues_link[start:end]
    
    return issues_link


@repeater
def select_issues(site, comic_link):
    if comic_link.url == "":
        return []

    issues_link = Core.get_issues_link_of_comic(site, comic_link.url)

    print(f"\nThis comic has {len(issues_link)} issues!")

    print("\nSelect the option you want:", "\n1.- Download one issue.")
    print("2.- Download a range of issues.", "\n3.- Download all issues.")

    choice = input("-- ")
    match choice.strip():
        case "1":
            issues_link = select_one_issue(issues_link)
        case "2":
            issues_link = select_range_of_issues(issues_link)
        case "3":
            pass
        case _:
            print("\nThat operation isn't exist. Try again")

    return issues_link


def download_comics():
    site = select_site()
    comic_link = search_comic(site)
    issues_link = select_issues(site, comic_link)

    create_folder_in_path(".", "Comics")

    comic_name = comic_link.tag

    if not comic_link.url == "":
        create_folder_in_path("./Comics/", comic_name)

    for link in issues_link:
        issue_name = link.tag
        issue_url = link.url

        create_folder_in_path(f"./Comics/{comic_name}", issue_name)

        issue_path = f"./Comics/{comic_name}/{issue_name}"
        
        images_link = Core.get_all_images_link_of_issue(site, issue_url)
        images_link = list(enumerate(images_link))

        for i, im_link in progressbar(images_link, f"{issue_name}: "):
            req_content = requests.get(im_link).content

            with open(f"{issue_path}/image{i}.jpg", "wb+") as img:
                img.write(req_content)

    return
