from ..base import JsonBased
from dataclasses import dataclass
from .view_type import ViewType

@dataclass
class ViewsType(JsonBased):
    view: ViewType
    url: str = "https://stepik.org/api/views"
    method: str = "POST"