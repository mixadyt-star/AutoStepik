from abc import ABC, abstractmethod

class AiClient(ABC):
    @abstractmethod
    def get_answer(self, prompt: str) -> str: ...