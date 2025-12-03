from abc import ABC, abstractmethod
from typing import Dict, Optional, NoReturn


class HeadersManager(ABC):
    @abstractmethod
    def __init__(self, headers: Optional[Dict[str, str]] = None): ...

    @abstractmethod
    def get_headers(self) -> Dict[str, str]: ...

    @abstractmethod
    def set_header(self, header_name: str, header_value: str) -> NoReturn: ...