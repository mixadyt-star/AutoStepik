from .base import JsonBased
from dataclasses import dataclass

@dataclass
class LoginType(JsonBased):
    email: str
    password: str
    url: str = "https://stepik.org/api/users/login"
    method: str = "POST"