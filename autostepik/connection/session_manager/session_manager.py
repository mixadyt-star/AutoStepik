"""Module for abstract session manager class"""

from abc import ABC, abstractmethod


class SessionManager(ABC):
    """Stores and restores session in session variable"""

    @abstractmethod
    def load_session(self, session_file_path: str) -> None:
        """Loads session from provided path to variable session

        :param session_file_path: Path from which the session will be loaded
        :type session_file_path: str
        """

    @abstractmethod
    def save_session(self, session_file_path: str) -> None:
        """Saves session from variable session to provided path

        :param session_file_path: Path where the session will be saved
        :type session_file_path: str
        """
