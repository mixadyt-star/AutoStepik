from dataclasses import dataclass
from typing import List, Dict, Any
from .course_actions import CourseActions

@dataclass
class Course:
    id: int
    summary: str
    workload: str
    cover: str
    intro: str
    course_format: str
    target_audience: str
    certificate_footer: str | None
    certificate_cover_org: str | None
    is_certificate_issued: bool
    is_certificate_auto_issued: bool
    certificate_regular_threshold: int | None
    certificate_distinction_threshold: int | None
    instructors: List[int]
    certificate: str
    requirements: str
    description: str
    sections: List[int]
    total_units: int
    enrollment: int
    is_favorite: bool
    actions: CourseActions
    progress: str
    first_lesson: int
    first_unit: int
    certificate_link: str | None
    certificate_regular_link: str | None
    certificate_distinction_link: str | None
    user_certificate: str | None
    referral_link: str | None
    schedule_link: str | None
    schedule_long_link: str | None
    first_deadline: str | None
    last_deadline: str | None
    subscriptions: List[str]
    announcements: List[int]
    is_contest: bool
    is_self_paced: bool
    is_adaptive: bool
    is_idea_compatible: bool
    is_in_wishlist: bool
    last_step: str
    intro_video: str | None
    social_providers: List[str]
    authors: List[int]
    tags: List[int]
    has_tutors: bool
    is_enabled: bool
    is_proctored: bool
    proctor_url: str | None
    review_summary: int
    schedule_type: str | None
    certificates_count: int
    learners_count: int
    lessons_count: int
    quizzes_count: int
    challenges_count: int
    peer_reviews_count: int
    instructor_reviews_count: int
    videos_duration: int
    time_to_complete: int
    is_popular: bool
    is_processed_with_paddle: bool
    is_unsuitable: bool
    is_paid: bool
    price: int | None
    currency_code: str | int | None
    display_price: str
    default_promo_code_name: str | None
    default_promo_code_price: int | None
    default_promo_code_discount: int | None
    default_promo_code_is_percent_discount: bool | None
    default_promo_code_expire_date: str | None
    continue_url: str
    readiness: float
    is_archived: bool
    options: Dict[Any, Any]
    price_tier: None
    position: int
    is_censored: bool
    difficulty: str | None
    acquired_skills: List[str]
    acquired_assets: List[Any]
    learning_format: str
    content_details: List[Any]
    issue: None
    course_type: str
    possible_type: None
    is_certificate_with_score: bool
    preview_lesson: int | None
    preview_unit: int | None
    possible_currencies: List[Any]
    commission_basic: None
    commission_promo: None
    with_certificate: bool
    child_courses: List[Any]
    child_courses_count: int
    parent_courses: List[Any]
    became_published_at: str
    became_paid_at: None
    title_en: str
    last_update_price_date: None
    owner: int
    language: str
    is_featured: bool
    is_public: bool
    canonical_url: str
    title: str
    slug: str
    begin_date: str | None
    end_date: str | None
    soft_deadline: None
    hard_deadline: None
    grading_policy: str
    begin_date_source: str | None
    end_date_source: str | None
    soft_deadline_source: None
    hard_deadline_source: None
    grading_policy_source: str
    is_active: bool
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
    lti_consumer_key: str
    lti_secret_key: str
    lti_private_profile: bool