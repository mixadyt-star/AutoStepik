from ...stepik_client import StepikClient
from .solver import Solver
from typing import NoReturn

class CodeSolver(Solver):
    def send_code(self, attempt_id: int, code: str, stepik_client: StepikClient) -> NoReturn:
        stepik_client.create_new_solution(
            attempt_id=attempt_id,
            code=code,
        )
