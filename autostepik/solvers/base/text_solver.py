from ...stepik_client import StepikClient
from .solver import Solver
from typing import NoReturn

class TextSolver(Solver):
    def send_text(self, step_id: int, assignment_id: int, stepik_client: StepikClient) -> NoReturn:
        stepik_client.set_view(
            step_id=step_id,
            assignment_id=assignment_id,
        )
