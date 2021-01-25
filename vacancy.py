class Vacancy:
    title = ''
    link = ''
    location = ''
    description = ''
    salary = '0'
    company = ''

    def __init__(
        self,
        title='',
        link='',
        location='',
        description='',
        company='',
        salary='0'
    ):
        self.title = title.strip()
        self.link = link.strip()
        self.location = location.strip()
        self.description = description
        self.salary = salary.strip()
        self.company = company.strip()
