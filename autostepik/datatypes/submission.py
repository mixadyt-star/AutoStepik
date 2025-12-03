from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Submission:
    id: int
    status: str
    score: float
    hint: str
    feedback: Dict[Any, Any] | str
    time: str
    reply: Dict[Any, Any]
    reply_url: None
    attempt: int
    session: None
    eta: int | float