from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SolutionReplyType:
    blanks: Optional[List[str]] = None
    ordering: Optional[List[int]] = None
    text: Optional[str] = None
    choices: Optional[List[bool]] = None
    code: Optional[str] = None
    language: Optional[str] = None