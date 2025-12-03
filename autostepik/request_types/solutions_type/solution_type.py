from dataclasses import dataclass
from .solution_reply_type import SolutionReplyType

@dataclass
class SolutionType:
    eta: None
    has_session: bool
    hint: None
    reply: SolutionReplyType
    reply_url: None
    score: None
    session_id: None
    status: None
    time: None
    attempt: int 
    session: None