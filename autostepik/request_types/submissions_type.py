from .base import URLParamBased
from dataclasses import dataclass

@dataclass
class SubmissionsType(URLParamBased):
    limit: int
    order: str
    step: int
    user: int
    url: str = "https://stepik.org/api/submissions?"
    method: str = "GET"