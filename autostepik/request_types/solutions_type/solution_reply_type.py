from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class SolutionReplyType:
    number: Optional[int] = None
    blanks: Optional[List[str]] = None
    ordering: Optional[List[int]] = None
    text: Optional[str] = None
    choices: Optional[List[bool]] | Optional[Dict[Any, Any]] = None
    code: Optional[str] = None
    language: Optional[str] = None