from headers_generator import HeaderGenerator
from page_query_generator import PageQueryGenerator
from url_generator import UrlGenerator
import requests
from bs4 import BeautifulSoup


class Parser:

    headers = {}
    url = ''
    max_page = 0

    def __init__(self, source=''):
        self.source = source
        self.headers = HeaderGenerator.get_headers()
        self.url = UrlGenerator.get_url(source=source, search='')

    def request_page(self, page_number=0):
        current_url = f'{self.url}{PageQueryGenerator.get_page_query(source=self.source,page_number=page_number)}'
        content = None
        response = requests.get(current_url, headers=self.headers)

        if response.status_code == 200:
            content = BeautifulSoup(response.text, 'html.parser')

        return content

    def get_max_page(self):
        return self.request_page()
        # find max page make in children class
        # self.max_page = ...

    def get_jobs(self):
        # jobs = []
        self.get_max_page()
        for page in range(self.max_page):
            pass
            # content = self.request_page(page=page)
            # find job items
        # return jobs
