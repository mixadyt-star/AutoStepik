from dataclasses import dataclass
from .attempt_dataset import AttemptDataset

@dataclass
class Attempt:
    id: int
    dataset: AttemptDataset | str | None
    dataset_url: None
    time: str
    status: str
    time_left: None
    step: int
    user: int