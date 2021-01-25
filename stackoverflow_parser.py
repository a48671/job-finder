from parser import Parser
from url_generator import UrlGenerator
from vacancy import Vacancy


class StackoverflowParser(Parser):
    def __init__(self, search=''):
        super().__init__(source='stackoverflow')
        self.url = UrlGenerator.get_url('stackoverflow', search)

    def get_max_page(self):
        page_soup = super().get_max_page()
        paginator = page_soup.find_all('a', {
            'class': 's-pagination--item'
        })
        pages = []

        for item in paginator:
            page_number = item.text.strip()
            if page_number.isdigit():
                pages.append(int(page_number))

        self.max_page = pages[-1]

        return self.max_page

    def get_jobs(self):
        jobs = []
        self.get_max_page()
        for page_number in range(1, self.max_page + 1):
            page_soup = self.request_page(page_number=page_number)
            vacancy_list = page_soup.find_all('div', {'class': '-job'})
            for vacancy in vacancy_list:
                title = vacancy.find('h2').text
                link = f'https://stackoverflow.com/{vacancy.find("h2").find("a")["href"]}'
                company_data = vacancy.find('h3').find_all('span', recursive=False)
                location = company_data[1].text
                company = company_data[0].text
                jobs.append(Vacancy(
                    title=title,
                    link=link,
                    location=location,
                    company=company,
                    salary='',
                    description=''
                ))
        return jobs
