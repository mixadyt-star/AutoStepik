from .html_parser import HTMLParser
from bs4 import BeautifulSoup

class SelfIDParser(HTMLParser):
    @staticmethod
    def parse(html):
        parser = BeautifulSoup(html, "html.parser")
        header = parser.find("header")
        profile_link_element = header.find(class_="navbar__logo-link")
        profile_link = profile_link_element.attrs["href"]
        
        return int(profile_link.split("/")[2])