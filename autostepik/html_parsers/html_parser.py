from abc import ABC, abstractmethod
from typing import Any

class HTMLParser(ABC):
    @staticmethod
    @abstractmethod
    def parse(html: str) -> Any: ...