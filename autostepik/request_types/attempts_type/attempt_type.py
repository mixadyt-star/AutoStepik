from dataclasses import dataclass

@dataclass
class AttemptType:
    dataset_url: None
    status: None
    time: None
    time_left: None
    user_id: None
    step: int
    user: int | None