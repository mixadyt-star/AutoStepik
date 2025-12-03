from abc import ABC, abstractmethod
from typing import Optional
from ..session_manager import SessionManager
from ..headers_manager import HeadersManager
from requests import Response
from ..request_types import Base


class Connection(ABC):
    @abstractmethod
    def __init__(self, session_manager: Optional[SessionManager] = None, headers_manager: Optional[HeadersManager] = None): ...

    @abstractmethod
    def get_response(self, datatype: Base, **kwargs) -> Response: ...