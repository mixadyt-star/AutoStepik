"""Module for abstract headers manager class"""

from abc import ABC, abstractmethod
from typing import Dict


class HeadersManager(ABC):
    """Stores and restores headers"""

    @abstractmethod
    def get_headers(self) -> Dict[str, str]:
        """Returns stored headers

        :return: Stored headers
        :rtype: Dict[str, str]
        """

    @abstractmethod
    def set_header(self, name: str, value: str) -> None:
        """Sets / updates header with name to value

        :param name: Update header's name
        :type name: str
        :param value: Update header's value
        :type value: str
        """
