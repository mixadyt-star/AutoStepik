from .base import EmptyBased
from dataclasses import dataclass

@dataclass
class MainType(EmptyBased):
    url: str = "https://stepik.org/"
    method: str = "GET"