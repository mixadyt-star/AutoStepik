from dataclasses import asdict
from urllib.parse import urlencode
from .base import RequestBase

class URLParamBased(RequestBase):
    def build(self):
        url_body = asdict(self)
        url = url_body.pop("url")
        method = url_body.pop("method")

        params = []

        for key, value in url_body.items():
            if isinstance(value, list):
                params.extend((f"{key}[]", item) for item in value)

            else:
                params.append((key, value))

        return {
            "url": url + urlencode(params),
            "method": method,
        }