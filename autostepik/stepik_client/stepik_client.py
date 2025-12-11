from abc import ABC, abstractmethod
from ..datatypes import UserCourse, Course, Section, Unit, Lesson, Step, Progress, Attempt, Submission, Assignment
from typing import NoReturn, Optional, List


class StepikClient(ABC):
    @abstractmethod
    def login(self, email: str, password: str) -> NoReturn: ...

    @abstractmethod
    def get_self_id(self) -> int: ...

    @abstractmethod
    def get_user_courses(self) -> List[UserCourse]: ...

    @abstractmethod
    def get_courses(self, ids: List[int]) -> List[Course]: ...

    @abstractmethod
    def get_section(self, id: int) -> Section: ...

    @abstractmethod
    def get_unit(self, id: int) -> Unit: ...

    @abstractmethod
    def get_lesson(self, id: int) -> Lesson: ...

    @abstractmethod
    def get_steps(self, ids: List[int]) -> List[Step]: ...

    @abstractmethod
    def get_progresses(self, ids: List[str]) -> List[Progress]: ...

    @abstractmethod
    def create_new_attempt(self, step_id: int) -> Attempt: ...

    @abstractmethod
    def create_new_solution(self, attempt_id: int, code: Optional[str] = None, choices: Optional[List[bool]] = None, text: Optional[str] = None, ordering: Optional[List[int]] = None, blanks: Optional[List[str]] = None) -> NoReturn: ...

    @abstractmethod
    def get_submissions(self, limit: int, step_id: int, user_id: int) -> List[Submission]: ...

    @abstractmethod
    def set_view(self, step_id: int, assignment_id: int) -> NoReturn: ...

    @abstractmethod
    def get_assignments(self, ids: List[int]) -> List[Assignment]: ...