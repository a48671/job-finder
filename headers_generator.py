class HeaderGenerator:

    @staticmethod
    def get_headers(
            hosts='hh.ru',
            user_agent='Safari',
            accept='*/*',
            accept_encoding='gzip,deflate, br',
            connection='keep-alive'
    ):

        return {
            'Hosts': hosts,
            'User-Agent': user_agent,
            'Accept': accept,
            'Accept-Encoding': accept_encoding,
            'Connection': connection
        }
