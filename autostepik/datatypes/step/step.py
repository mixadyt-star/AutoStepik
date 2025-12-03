from dataclasses import dataclass
from .step_block import StepBlock
from .step_actions import StepActions
from typing import List


@dataclass
class Step:
    id: int
    lesson: int
    position: int
    status: str
    block: StepBlock
    actions: StepActions
    progress: str
    subscriptions: List[str]
    instruction: None
    session: None
    instruction_type: None
    viewed_by: int
    passed_by: int
    correct_ratio: float | None
    worth: int
    is_solutions_unlocked: bool
    solutions_unlocked_attempts: int
    has_submissions_restrictions: bool
    max_submissions_count: int
    variation: int
    variations_count: int
    is_enabled: bool
    needs_plan: None
    num_grades: List[int]
    user_step_grade: None
    user_step_vote: None
    create_date: str
    update_date: str
    discussions_count: int
    discussion_proxy: str
    discussion_threads: List[str]