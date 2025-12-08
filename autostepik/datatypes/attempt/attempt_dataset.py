"""Attempt dataset module"""

from dataclasses import dataclass
from typing import List

@dataclass
class AttemptDataset:
    """Attempt dataset model for attempt model"""

    is_multiple_choice: bool
    options: List[str]
