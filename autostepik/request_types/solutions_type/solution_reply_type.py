from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SolutionReplyType:
    choices: Optional[List[bool]] = None
    code: Optional[str] = None
    language: Optional[str] = None