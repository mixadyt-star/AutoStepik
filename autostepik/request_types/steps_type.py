from .base import URLParamBased
from dataclasses import dataclass
from typing import List

@dataclass
class StepsType(URLParamBased):
    ids: List[int]
    url: str = "https://stepik.org/api/steps?"
    method: str = "GET"