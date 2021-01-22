from headers_generator import HeaderGenerator
from url_generator import UrlGenerator
import requests


class Parser:

    headers = {}
    url = ''

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
