from .base import URLBased
from dataclasses import dataclass

@dataclass
class SectionsType(URLBased):
    id: int
    url: str = "https://stepik.org/api/sections/"
    method: str = "GET"