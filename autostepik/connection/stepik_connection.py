from ..session_manager import DefaultSessionManager
from ..headers_manager import StepikHeadersManager

class StepikConnection:
    def __init__(self, session_manager = None, headers_manager = None):
        self.session_manager = session_manager or DefaultSessionManager()
        self.headers_manager = headers_manager or StepikHeadersManager()

    def get_response(self, datatype, **kwargs):
        response = self.session_manager.session.request(headers=self.headers_manager.get_headers(), **datatype.build(), **kwargs)
        
        self.headers_manager.set_header(
            "X-CSRFToken",
            self.session_manager.session.cookies.get("csrftoken"),
        )

        return response