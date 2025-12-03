from .base import URLBased
from dataclasses import dataclass

@dataclass
class LessonsType(URLBased):
    id: int
    url: str = "https://stepik.org/api/lessons/"
    method: str = "GET"