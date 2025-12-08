"""Module that implements stepik connection class"""

from .session_manager import DefaultSessionManager
from .headers_manager import StepikHeadersManager
from .connection import Connection

class StepikConnection(Connection):
    """Sends requests to stepik and updates session and headers"""

    def __init__(self, session_manager = None, headers_manager = None):
        self.session_manager = session_manager or DefaultSessionManager()
        self.headers_manager = headers_manager or StepikHeadersManager()

    def get_response(self, request, **kwargs):
        response = self.session_manager.session.request(
            headers=self.headers_manager.get_headers(),
            **request.build(),
            **kwargs,
        )

        self.headers_manager.set_header(
            name="X-CSRFToken",
            value=self.session_manager.session.cookies.get("csrftoken"),
        )

        return response
