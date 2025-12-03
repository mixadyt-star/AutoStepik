from .stepik_client import StepikClient
from ..connection import StepikConnection
from ..request_types import MainType, LoginType, CatalogType, UserCoursesType, CoursesType, SectionsType, UnitsType, LessonsType, StepsType, ProgressesType, AttemptsType, AttemptType, SolutionReplyType, SolutionType, SolutionsType, SubmissionsType, ViewsType, ViewType, AssignmentsType
from ..html_parser import SelfIDParser
from ..datatypes import UserCourse, Course, Section, Unit, Lesson, Step, Progress, Attempt, Submission, Assignment
from dacite import from_dict



class DefaultStepikClient(StepikClient):
    def __init__(self, connection = None):
        self.connection = connection or StepikConnection()

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

        return [from_dict(UserCourse, user_course) for user_course in response.json()["user-courses"]]

    def get_courses(self, ids):
        response = self.connection.get_response(
            CoursesType(
                ids=ids,
            )
        )

        return [from_dict(Course, course) for course in response.json()["courses"]]
    
    def get_section(self, id):
        response = self.connection.get_response(
            SectionsType(
                id=id,
            )
        )

        return from_dict(Section, response.json()["sections"][0])
    
    def get_unit(self, id):
        response = self.connection.get_response(
            UnitsType(
                id=id,
            )
        )

        return from_dict(Unit, response.json()["units"][0])
    
    def get_lesson(self, id):
        response = self.connection.get_response(
            LessonsType(
                id=id,
            )
        )

        return from_dict(Lesson, response.json()["lessons"][0])
    
    def get_steps(self, ids):
        response = self.connection.get_response(
            StepsType(
                ids=ids
            )
        )

        return [from_dict(Step, step) for step in response.json()["steps"]]
    
    def get_progresses(self, ids):
        response = self.connection.get_response(
            ProgressesType(
                ids=ids,
            )
        )

        return [from_dict(Progress, progress) for progress in response.json()["progresses"]]

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

        return from_dict(Attempt, response.json()["attempts"][0])
    
    def create_new_solution(self, attempt_id, code = None, choices = None, text = None):
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

        return [from_dict(Submission, submission) for submission in response.json()["submissions"]]
    
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

        return [from_dict(Assignment, assignment) for assignment in response.json()["assignments"]]