"""Module that provides stepik headers manager class"""

from .headers_manager import HeadersManager

class StepikHeadersManager(HeadersManager):
    """Stores and restores headers. Has default headers"""

    def __init__(self, headers = None):
        self.headers = headers or {
            "Accept": "*/*",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json; charset=UTF-8",
            "Origin": "https://stepik.org",
            "Referer": "https://stepik.org/catalog?auth=login",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) "
            "Gecko/20100101 Firefox/145.0",
        }

    def get_headers(self):
        return self.headers

    def set_header(self, name, value):
        self.headers[name] = value
