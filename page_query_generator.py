class PageQueryGenerator:

    @staticmethod
    def get_page_query(source: str, page_number) -> str:
        if source == 'hh':
            return f'&page={page_number}'
        elif source == 'stackoverflow':
            return f'&pg={page_number}'
        else:
            return ''
