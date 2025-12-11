"""Attempt dataset module"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class AttemptDataset:
    """Attempt dataset model for attempt model"""

    is_multiple_choice: Optional[bool] = None
    options: Optional[List[str]] = None
    pairs: Optional[List[Dict[str, str]]] = None
