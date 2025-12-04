from ...stepik_client import StepikClient
from .solver import Solver
from typing import NoReturn, List

class SortingSolver(Solver):
    def send_ordering(self, attempt_id: int, ordering: List[int], stepik_client: StepikClient) -> NoReturn:
        stepik_client.create_new_solution(
            attempt_id=attempt_id,
            ordering=ordering,
        )
