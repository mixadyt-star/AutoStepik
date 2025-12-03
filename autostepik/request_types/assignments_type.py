from .base import URLParamBased
from dataclasses import dataclass
from typing import List

@dataclass
class AssignmentsType(URLParamBased):
    ids: List[int]
    url: str = "https://stepik.org/api/assignments?"
    method: str = "GET"