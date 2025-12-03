from dataclasses import dataclass


@dataclass
class Assignment:
    id: int
    unit: int
    step: int
    progress: str
    create_date: str
    update_date: str