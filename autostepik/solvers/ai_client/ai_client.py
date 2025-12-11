from abc import ABC, abstractmethod

class AiClient(ABC):
    @abstractmethod
    def get_response(self, prompt: str) -> str: ...