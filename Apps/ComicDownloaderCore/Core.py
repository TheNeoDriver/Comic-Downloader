from Websites.Zipcomics import Zipcomics

WEBSITES = [
    Zipcomics()
]
"""Contain a instance of all websites classes."""


def get_all_comics_in_website(site = 0, comic_name = ""):
    """gets all comics that match with the comic name in the website
    specified by the site number (See WEBSITES constant).
    Returns a list of Links Objects"""

    comics_link = WEBSITES[site].get_comics_link(comic_name)
    return comics_link


def get_issues_link_of_comic(site = 0, comic_url = ""):
    """Gets all issue of a url with the specific method of a website
    deternined by the site number (See WEBSITES constant).
    Returns a list of Links Objects"""

    issues_link = WEBSITES[site].get_issues_link(comic_url)
    return issues_link


def get_all_images_link_of_issue(site = 0, issue_url = ""):
    """Gets all images of a issue url with the specific method of a website
    determined by the site number (See WEBSITES constant).
    Returns a list of Links Objects"""

    images_link = WEBSITES[site].get_images_link(issue_url)

    return images_link
