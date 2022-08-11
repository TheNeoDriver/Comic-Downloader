from Websites.Website import Website
from Websites.Link import Link
from bs4 import BeautifulSoup
import requests


class Zipcomics(Website):

    def __init__(self):
        super().__init__()
        self._name = "Zipcomics"
        self._url = "https://www.zipcomic.com"
    

    def get_comics_link(self, comic_name):

        search = "+".join(comic_name.split())
        url = f"{self._url}/search?kwd={search}"

        comics_link = self._get_setences_link(comic_name, url)
        comics_link = [link for link in comics_link if not "issue" in link.tag.lower()]
        comics_link = [link for link in comics_link if not link.tag.isdigit()]

        return comics_link
    

    def get_issues_link(self, url):
        issues_link = self._get_setences_link("issue", url)
        links = issues_link

        for i, link_a in enumerate(issues_link):
            coincidence = False

            for link_b in links[i+1:]:
                if link_a.tag == link_b.tag:
                    issues_link = links[i+1:]
                    coincidence = True
            
            if not coincidence:
                break

        for link in issues_link:
            link.tag = link.tag.strip()

        return issues_link
    

    def get_images_link(self, url):

        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        images = soup.findAll('img')

        images_link = [img["src"] for img in images]

        return images_link


    def _get_setences_link(self, sentence, url):
        links = []

        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        a_objects = soup.find_all("a")
        for a in a_objects:
            a.string = "" if a.string is None else a.string

            if sentence in a.string.lower():
                link = Link()
                link.tag = f"{a.string}"
                link.url = self._url + a["href"]

                links.append(link)
        
        return links
