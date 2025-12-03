from .base import URLParamBased
from dataclasses import dataclass

@dataclass
class UserCoursesType(URLParamBased):
    is_archived: bool
    is_assistant: bool
    limit: int
    page: int
    url: str = "https://stepik.org/api/user-courses?"
    method: str = "GET"