class UrlGenerator:

    @staticmethod
    def get_url(source: str, search: str) -> str:
        if source == 'hh':
            items = 100
            return f'https://hh.ru/search/vacancy?st=searchVacancy&text={search}&items_on_page={items}'
        elif source == 'stackoverflow':
            return f'https://stackoverflow.com/jobs?q={search}'
        else:
            return ''
