from bs4 import BeautifulSoup
import requests


def div_tag(tag):
    return tag.name == "div" and tag.has_attr("id") and "txt_d" in tag["id"]


class NamesDaySiteParser:
    PAGE_URL = "https://imienniczek.pl"

    def __init__(self):
        self.parsed_page = None
        self.found_names = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")

    def parse_all_names(self):
        names = self.parsed_page.find(id="txt_d")
        names = names.find_all("a")
        for name in names:
            self.found_names.append(name.string)


def show_todays_names():
    parser = NamesDaySiteParser()
    parser.load_page_html()
    parser.parse_all_names()
    print(f"Dzisiaj imieniny obchodzą: ", end="")
    for name in parser.found_names:
        print(name, end="")
        if name != parser.found_names[-1]:
            print(end=", ")
        else:
            print(".")
