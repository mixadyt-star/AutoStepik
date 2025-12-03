from ...stepik_client import StepikClient
from .solver import Solver
from typing import NoReturn, List

class ChoiceSolver(Solver):
    def send_choices(self, attempt_id: int, choices: List[bool], stepik_client: StepikClient) -> NoReturn:
        stepik_client.create_new_solution(
            attempt_id=attempt_id,
            choices=choices,
        )
