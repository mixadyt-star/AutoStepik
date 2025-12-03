from dataclasses import dataclass
from typing import Optional

@dataclass
class CourseAction:
    enabled: bool
    needs_permission: Optional[str] = None