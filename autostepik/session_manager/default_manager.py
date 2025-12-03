from .session_manager import SessionManager
from requests import Session
import pickle
import os

class DefaultSessionManager(SessionManager):
    def __init__(self):
        self.session = Session()

    def load_session(self, session_file_path):
        if (os.path.exists(session_file_path)):

            if (os.path.isfile(session_file_path)):

                with open(session_file_path, "rb") as session_dump:
                    self.session = pickle.load(session_dump)
                
            else:
                raise IsADirectoryError("Path %s leads to directory" % session_file_path)
            
        else:
            raise FileNotFoundError("Session dump on path %s not found" % session_file_path)
        
    def save_session(self, session_file_path):
        with open(session_file_path, "wb") as session_dump:
            pickle.dump(self.session, session_dump)