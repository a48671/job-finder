from parser import Parser
from url_generator import UrlGenerator


class HeadHunterParser(Parser):

    def __init__(self):
        super().__init__()
        self.url = UrlGenerator.get_url('hh')


head_hunter_parser = HeadHunterParser()
