from typing import Optional

class DatatypeParseError(Exception):
    def __init__(self, message: Optional[str] = "Can't parse datatype."):
        self.message = message

        super().__init__(self.message)