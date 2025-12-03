from abc import ABC, abstractmethod
from typing import NoReturn

class Output(ABC):
    @staticmethod
    @abstractmethod
    def print(string: str) -> NoReturn: ...