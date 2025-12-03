from dataclasses import dataclass


@dataclass
class Progress:
    id: str
    last_viewed: int | None
    score: float
    cost: int
    n_steps: int
    n_steps_attempted: int
    n_steps_passed: int
    is_attempted: bool
    is_passed: bool
    is_exam_mode: bool