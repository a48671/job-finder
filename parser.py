from headers_generator import HeaderGenerator
from url_generator import UrlGenerator
import requests
from bs4 import BeautifulSoup


class Parser:

    headers = {}
    url = ''
    max_page = 0

    def __init__(self):
        self.headers = HeaderGenerator.get_headers()
        self.url = UrlGenerator.get_url(source='')

    def request_page(self, page=0):
        current_url = f'{self.url}&page={page}'
        content = ''
        response = requests.get(current_url, headers=self.headers)

        if response.status_code == 200:
            content = response.text

        return content

    def get_max_page(self):
        page = self.request_page()
        return BeautifulSoup(page, 'html.parser')
        # find max page make in children class
        # self.max_page = ...

    def get_jobs(self):
        self.get_max_page()
        for page in range(self.max_page):
            content = self.request_page(page=page)
            print(BeautifulSoup(content, 'html.parser').title)
