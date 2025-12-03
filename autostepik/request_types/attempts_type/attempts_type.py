from .attempt_type import AttemptType
from ..base import JsonBased
from dataclasses import dataclass

@dataclass
class AttemptsType(JsonBased):
    attempt: AttemptType
    url: str = "https://stepik.org/api/attempts"
    method: str = "POST"