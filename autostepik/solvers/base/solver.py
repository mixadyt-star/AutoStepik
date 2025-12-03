from ...datatypes import Step
from ...stepik_client import StepikClient
from abc import ABC, abstractmethod
from typing import NoReturn

class Solver(ABC):
    @abstractmethod
    def solve(self, step: Step, assignment_id: int, user_id: int, stepik_client: StepikClient) -> NoReturn: ...