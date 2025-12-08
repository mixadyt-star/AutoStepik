"""Attempt dataclass module"""

from dataclasses import dataclass
from .attempt_dataset import AttemptDataset

@dataclass
class Attempt:
    """Task attempt model"""

    id: int
    dataset: AttemptDataset | None
    dataset_url: None
    time: str
    status: str
    time_left: None
    step: int
    user: int
