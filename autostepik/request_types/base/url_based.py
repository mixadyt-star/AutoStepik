from dataclasses import asdict
from urllib.parse import quote
from .base import RequestBase

class URLBased(RequestBase):
    def build(self):
        url_body = asdict(self)
        url = url_body.pop("url")
        method = url_body.pop("method")

        return {
            "url": url + quote(
                str(
                    list(
                        url_body.values()
                    )[0]
                )
            ),
            "method": method,
        }