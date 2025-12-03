from .base import URLParamBased
from dataclasses import dataclass
from typing import List

@dataclass
class CoursesType(URLParamBased):
    ids: List[int]
    url: str = "https://stepik.org/api/courses?"
    method: str = "GET"