from .base import EmptyBased
from dataclasses import dataclass

@dataclass
class CatalogType(EmptyBased):
    url: str = "https://stepik.org/catalog?auth=login"
    method: str = "GET"