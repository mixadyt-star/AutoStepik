"""Module that implements default session manager class"""

import pickle
import os
from requests import Session
from .session_manager import SessionManager

class DefaultSessionManager(SessionManager):
    """Stores and restores session in session variable"""

    def __init__(self):
        self.session = Session()

    def load_session(self, session_file_path):
        if os.path.exists(session_file_path):

            if os.path.isfile(session_file_path):

                with open(session_file_path, "rb") as session_dump:
                    self.session = pickle.load(session_dump)

            else:
                raise IsADirectoryError(f"Path {session_file_path} leads to directory")

        else:
            raise FileNotFoundError(f"Session dump on path {session_file_path} not found")

    def save_session(self, session_file_path):
        with open(session_file_path, "wb") as session_dump:
            pickle.dump(self.session, session_dump)
