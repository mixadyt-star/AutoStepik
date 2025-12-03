from ...stepik_client import StepikClient
from .solver import Solver
from typing import NoReturn

class StringSolver(Solver):
    def send_string(self, attempt_id: int, text: str, stepik_client: StepikClient) -> NoReturn:
        stepik_client.create_new_solution(
            attempt_id=attempt_id,
            text=text,
        )
