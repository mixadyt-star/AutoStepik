from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Section:
    id: int
    course: int
    units: List[int]
    position: int
    discounting_policy: str
    progress: str
    actions: Dict[Any, Any]
    required_section: int | None
    required_percent: int
    is_requirement_satisfied: bool
    is_exam: bool
    is_exam_without_progress: bool
    is_random_exam: bool
    exam_duration_minutes: int
    random_exam_problems_course: None
    random_exam_problems_count: int
    exam_session: int | None
    proctor_session: None
    description: str
    is_proctoring_can_be_scheduled: bool
    title: str
    slug: str
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