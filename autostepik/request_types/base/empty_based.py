from .base import Base

class EmptyBased(Base):
    def build(self):
        return {
            "url": self.url,
            "method": self.method,
        }