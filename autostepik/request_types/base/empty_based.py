from .base import RequestBase

class EmptyBased(RequestBase):
    def build(self):
        return {
            "url": self.url,
            "method": self.method,
        }