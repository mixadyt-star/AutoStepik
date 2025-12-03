from .base import URLBased
from dataclasses import dataclass

@dataclass
class UnitsType(URLBased):
    id: int
    url: str = "https://stepik.org/api/units/"
    method: str = "GET"