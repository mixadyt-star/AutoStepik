from abc import ABC, abstractmethod
from ...datatypes import Step, Attempt

class PromptGenerator(ABC):
    @abstractmethod
    def generate_prompt(self, step: Step, attempt: Attempt, task_type: str) -> str: ...