from dataclasses import asdict
from .base import Base

class JsonBased(Base):
    def build(self):
        json_body = asdict(self)
        url = json_body.pop("url")
        method = json_body.pop("method")

        return {
            "url": url,
            "method": method,
            "json": json_body,
        }