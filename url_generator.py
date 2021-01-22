class UrlGenerator:

    @staticmethod
    def get_url(source: str) -> str:
        if source == 'hh':
            items = 100
            return f'https://hh.ru/search/vacancy?st=searchVacancy&text=react&items_on_page={items}'
        else:
            return ''
