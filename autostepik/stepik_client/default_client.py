from .stepik_client import StepikClient
from ..connection import Connection, StepikConnection
from ..request_types import MainType, LoginType, CatalogType, UserCoursesType, CoursesType, SectionsType, UnitsType, LessonsType, StepsType, ProgressesType, AttemptsType, AttemptType, SolutionReplyType, SolutionType, SolutionsType, SubmissionsType, ViewsType, ViewType, AssignmentsType
from ..html_parsers import SelfIDParser
from ..datatypes import UserCourse, Course, Section, Unit, Lesson, Step, Progress, Attempt, Submission, Assignment
from ..datatype_parsers import DatatypeParser, DefaultDatatypeParser
from typing import Optional

class DefaultStepikClient(StepikClient):
    def __init__(self, connection: Optional[Connection] = None, datatype_parser: Optional[DatatypeParser] = None):
        self.connection = connection or StepikConnection()
        self.datatype_parser = datatype_parser or DefaultDatatypeParser()

        self.connection.get_response(
            MainType()
        ) # To collect csrf token

    def login(self, email, password):
        response = self.connection.get_response(
            LoginType(
                email=email,
                password=password,
            )
        )

        if (response.status_code != 204):
            raise ConnectionError(f"Can't log in, status code: {response.status_code}")
        
    def get_self_id(self):
        response = self.connection.get_response(
            CatalogType()
        )

        return SelfIDParser.parse(response.text)
    
    def get_user_courses(self):
        response = self.connection.get_response(
            UserCoursesType(
                is_archived=False,
                is_assistant=False,
                limit=1000,
                page=1,
            )
        )

        return self.datatype_parser.parse_list(UserCourse, response, "user-courses")

    def get_courses(self, ids):
        response = self.connection.get_response(
            CoursesType(
                ids=ids,
            )
        )

        return self.datatype_parser.parse_list(Course, response, "courses")
    
    def get_section(self, id):
        response = self.connection.get_response(
            SectionsType(
                id=id,
            )
        )

        return self.datatype_parser.parse(Section, response, "sections")
    
    def get_unit(self, id):
        response = self.connection.get_response(
            UnitsType(
                id=id,
            )
        )

        return self.datatype_parser.parse(Unit, response, "units")
    
    def get_lesson(self, id):
        response = self.connection.get_response(
            LessonsType(
                id=id,
            )
        )

        return self.datatype_parser.parse(Lesson, response, "lessons")
    
    def get_steps(self, ids):
        response = self.connection.get_response(
            StepsType(
                ids=ids
            )
        )

        return self.datatype_parser.parse_list(Step, response, "steps")
    
    def get_progresses(self, ids):
        response = self.connection.get_response(
            ProgressesType(
                ids=ids,
            )
        )

        return self.datatype_parser.parse_list(Progress, response, "progresses")

    def create_new_attempt(self, step_id):
        response = self.connection.get_response(
            AttemptsType(
                attempt=AttemptType(
                    dataset_url=None,
                    status=None,
                    time=None,
                    time_left=None,
                    user_id=None,
                    step=step_id,
                    user=None,
                ),
            )
        )

        if (response.status_code != 201):
            raise ConnectionError(f"Can't create new attempt, status code: {response.status_code}")

        return self.datatype_parser.parse(Attempt, response, "attempts")
    
    def create_new_solution(self, attempt_id, code = None, choices = None, text = None, ordering = None, blanks = None, number = None):
        if (code is not None):
            reply_type = SolutionReplyType(
                code=code,
                language="python3",
            )

        elif (choices is not None):
            reply_type = SolutionReplyType(
                choices=choices,
            )

        elif (text is not None):
            reply_type = SolutionReplyType(
                text=text,
            )

        elif (ordering is not None):
            reply_type = SolutionReplyType(
                ordering=ordering,
            )

        elif (blanks is not None):
            reply_type = SolutionReplyType(
                blanks=blanks,
            )

        elif (blanks is not None):
            reply_type = SolutionReplyType(
                number=number,
            )

        response = self.connection.get_response(
            SolutionsType(
                submission=SolutionType(
                    eta=None,
                    has_session=False,
                    hint=None,
                    reply=reply_type,
                    reply_url=None,
                    score=None,
                    session_id=None,
                    status=None,
                    time=None,
                    attempt=attempt_id,
                    session=None,
                ),
            )
        )

        if (response.status_code != 201):
            raise ConnectionError(f"Can't create new solution, status code: {response.status_code}")

    def get_submissions(self, limit, step_id, user_id):
        response = self.connection.get_response(
            SubmissionsType(
                limit=limit,
                order="desc",
                step=step_id,
                user=user_id,
            )
        )

        return self.datatype_parser.parse_list(Submission, response, "submissions")
    
    def set_view(self, step_id, assignment_id):
        response = self.connection.get_response(
            ViewsType(
                view=ViewType(
                    assignment=assignment_id,
                    step=step_id,
                ),
            )
        )

        if (response.status_code != 201):
            raise ConnectionError(f"Can't set new view, status code: {response.status_code}")
        
    def get_assignments(self, ids):
        response = self.connection.get_response(
            AssignmentsType(
                ids=ids
            )
        )

        return self.datatype_parser.parse_list(Assignment, response, "assignments")