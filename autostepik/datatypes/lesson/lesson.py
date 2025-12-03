from dataclasses import dataclass
from typing import List
from .lesson_actions import LessonActions


@dataclass
class Lesson:
    id: int
    steps: List[int]
    actions: LessonActions
    progress: str
    subscriptions: List[str]
    viewed_by: int
    passed_by: int
    time_to_complete: int
    cover_url: str
    is_comments_enabled: bool
    is_exam_without_progress: bool
    is_blank: bool
    is_draft: bool
    is_orphaned: bool
    courses: List[int]
    units: List[int]
    owner: int
    language: str
    is_featured: bool
    is_public: bool
    canonical_url: str
    title: str
    slug: str
    create_date: str
    update_date: str
    learners_group: None
    testers_group: None
    moderators_group: None
    assistants_group: None
    teachers_group: None
    admins_group: None
    discussions_count: int
    discussion_proxy: str
    discussion_threads: List[str]
    epic_count: int
    abuse_count: int
    vote_delta: int
    vote: str
    lti_consumer_key: str
    lti_secret_key: str
    lti_private_profile: bool