from parser import Parser
from url_generator import UrlGenerator
from vacancy import Vacancy


class HeadHunterParser(Parser):

    def __init__(self, search=''):
        super().__init__(source='hh')
        self.url = UrlGenerator.get_url('hh', search)

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

    def get_jobs(self):
        jobs = []
        self.get_max_page()
        for page_number in range(self.max_page):
            page_soup = self.request_page(page_number=page_number)
            vacancy_list = page_soup.find_all('div', 'vacancy-serp-item')
            for vacancy in vacancy_list:
                title = vacancy.find('a').text
                link = vacancy.find('a')['href']
                location = vacancy.find('span', 'vacancy-serp-item__meta-info').text.split(',')[0]
                company = vacancy.find('div', 'vacancy-serp-item__meta-info-company').text
                salary = vacancy.find('div', 'vacancy-serp-item__sidebar').find('span')
                if salary is not None:
                    salary = salary.text
                else:
                    salary = ''
                description = vacancy.select('div[data-qa="vacancy-serp__vacancy_snippet_responsibility"]')[0].text
                jobs.append(Vacancy(
                    title=title,
                    link=link,
                    location=location,
                    company=company,
                    salary=salary,
                    description=description
                ))
        return jobs
