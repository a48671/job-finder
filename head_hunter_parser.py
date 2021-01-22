from parser import Parser
from url_generator import UrlGenerator


class HeadHunterParser(Parser):

    def __init__(self):
        super().__init__()
        self.url = UrlGenerator.get_url('hh')

    def get_max_page(self):
        page_soup = super().get_max_page()
        paginator = page_soup.find_all('span', {
            'class': 'pager-item-not-in-short-range'
        })
        pages = []

        for item in paginator:
            pages.append(int(item.find('a').text))

        self.max_page = pages[-1]

        return self.max_page


head_hunter_parser = HeadHunterParser()
