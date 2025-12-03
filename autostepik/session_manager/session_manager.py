from abc import ABC, abstractmethod
from typing import NoReturn


class SessionManager(ABC):
    @abstractmethod
    def load_session(self, session_file_path: str) -> NoReturn: ...

    @abstractmethod
    def save_session(self, session_file_path: str) -> NoReturn: ...