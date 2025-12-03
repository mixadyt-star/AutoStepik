from .unit_actions import UnitActions
from dataclasses import dataclass
from typing import List

@dataclass
class Unit:
    id: int
    section: int
    lesson: int
    assignments: List[int]
    position: int
    actions: UnitActions
    progress: str | None
    begin_date: None
    end_date: None
    soft_deadline: None
    hard_deadline: None
    grading_policy: str
    begin_date_source: None
    end_date_source: None
    soft_deadline_source: None
    hard_deadline_source: None
    grading_policy_source: None
    is_active: bool
    create_date: str
    update_date: str