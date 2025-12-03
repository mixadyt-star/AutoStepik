from ..base import JsonBased
from dataclasses import dataclass
from .solution_type import SolutionType

@dataclass
class SolutionsType(JsonBased):
    submission: SolutionType
    url: str = "https://stepik.org/api/submissions"
    method: str = "POST"