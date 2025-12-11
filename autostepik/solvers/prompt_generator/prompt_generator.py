from abc import ABC, abstractmethod
from ...datatypes import Step, Attempt

class PromptGenerator(ABC):
    @abstractmethod
    def generate_code_prompt(self, step: Step, attempt: Attempt) -> str: ...

    @abstractmethod
    def generate_choice_prompt(self, step: Step, attempt: Attempt) -> str: ...

    @abstractmethod
    def generate_string_prompt(self, step: Step, attempt: Attempt) -> str: ...

    @abstractmethod
    def generate_sorting_prompt(self, step: Step, attempt: Attempt) -> str: ...