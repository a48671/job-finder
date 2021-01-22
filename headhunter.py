from bs4 import BeautifulSoup

from head_hunter_parser import head_hunter_parser


def extract_max_page():

    hh = head_hunter_parser.request_page()

    hh_soup = BeautifulSoup(hh, 'html.parser')

    paginator = hh_soup.find_all('span', {
        'class': 'pager-item-not-in-short-range'
    })

    pages = []

    for item in paginator:
        pages.append(int(item.find('a').text))

    return pages[-1]


def extract_hh_jobs(max_page):

    for page in range(max_page):
        content = head_hunter_parser.request_page(page=page)
        print(BeautifulSoup(content, 'html.parser').title)

