from dataclasses import dataclass
from .course_action import CourseAction

@dataclass
class CourseActions:
    view_reports: CourseAction
    edit_reports: CourseAction
    view_grade_book_page: CourseAction
    view_grade_book: CourseAction
    edit_lti: CourseAction
    edit_advanced_settings: CourseAction
    manage_permissions: CourseAction
    view_revenue: CourseAction
    can_be_bought: CourseAction
    can_be_price_changed: CourseAction
    can_be_deleted: CourseAction
    edit_tags: CourseAction