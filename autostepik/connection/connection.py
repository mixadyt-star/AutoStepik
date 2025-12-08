"""Module for abstract connection class"""

from abc import ABC, abstractmethod
from requests import Response
from ..request_types import RequestBase


class Connection(ABC):
    """Sends requests to server and updates local state"""

    @abstractmethod
    def get_response(self, request: RequestBase, **kwargs) -> Response:
        """Sends request and returns response

        :param request: Request that will be sent to the server
        :type request: RequestBase
        :return: Response that the server will return
        :rtype: Response
        """
