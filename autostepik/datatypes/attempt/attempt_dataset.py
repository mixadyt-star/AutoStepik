from dataclasses import dataclass
from typing import List

@dataclass
class AttemptDataset:
    is_multiple_choice: bool
    options: List[str]