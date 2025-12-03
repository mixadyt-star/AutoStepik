from .base import URLParamBased
from dataclasses import dataclass
from typing import List

@dataclass
class ProgressesType(URLParamBased):
    ids: List[int]
    url: str = "https://stepik.org/api/progresses?"
    method: str = "GET"