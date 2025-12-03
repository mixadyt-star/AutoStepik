from dataclasses import dataclass


@dataclass
class UserCourse:
    id: int
    user: int
    course: int
    is_favorite: bool
    is_pinned: bool
    is_archived: bool
    last_viewed: str
    can_be_reviewed: bool