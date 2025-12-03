from abc import ABC, abstractmethod

class Input(ABC):
    @staticmethod
    @abstractmethod
    def read_line() -> str: ...