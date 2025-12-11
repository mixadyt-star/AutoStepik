"""Attempt dataclass module"""

from dataclasses import dataclass
from .attempt_dataset import AttemptDataset
from typing import Dict, Any

@dataclass
class Attempt:
    """Task attempt model"""

    id: int
    dataset: AttemptDataset | Dict[str, Any] | str | None
    dataset_url: None
    time: str
    status: str
    time_left: None
    step: int
    user: int
