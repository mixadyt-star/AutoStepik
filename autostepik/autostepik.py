from .stepik_client import StepikClient, DefaultStepikClient
from .input_output import Input, Output, ConsoleInputOutput
from .datatypes import Course, Section, Unit, Step, Progress
from .solvers import Solver
from typing import Optional, NoReturn
from .logger import logger
import traceback
from concurrent.futures import ThreadPoolExecutor

class AutoStepik:
    def __init__(self, email: str, password: str, solver: Solver, max_workers: Optional[int] = 2, stepik_client: Optional[StepikClient] = None, input_output: Optional[Input | Output] = None):
        self.email = email
        self.password = password
        self.solver = solver

        self.id: int | None = None
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

        try:
            self.stepik_client = stepik_client or DefaultStepikClient()
            self.input_output = input_output or ConsoleInputOutput()

        except Exception as e:
            logger.critical("Init auto stepik client failed")
            logger.debug(traceback.format_exc())
            exit()

        try:
            self.stepik_client.login(
                email=self.email,
                password=self.password,
            )
            logger.info("Loged in successfully")
        
        except Exception as e:
            logger.critical("Can't log in")
            logger.debug(traceback.format_exc())
            exit()

        try:
            self.id = self.stepik_client.get_self_id()
            logger.info("Got self id successfully")

        except Exception as e:
            logger.critical("Can't get self id")
            logger.debug(traceback.format_exc())
            exit()

    def solve(self) -> NoReturn:
        try:
            user_courses = self.stepik_client.get_user_courses()
            courses = self.stepik_client.get_courses(
                ids=[user_course.course for user_course in user_courses],
            )
            logger.info("Parsed courses successfully")
        
        except Exception as e:
            logger.critical("During parsing courses, error occured")
            logger.debug(traceback.format_exc())
            exit()

        self.input_output.print("Choose course: \n")
        for i, course in enumerate(courses):
            self.input_output.print(f"\t{i + 1}. {course.title}\n")

        self.input_output.print("AutoStepik > ")

        choose = int(self.input_output.read_line())

        self.solve_course(courses[choose - 1])

    def solve_course(self, course: Course) -> NoReturn:
        logger.info(f"Solving course {course.title}...")
        for section_id in course.sections:
            try:
                section = self.stepik_client.get_section(section_id)

                if (section.is_active):
                    self.solve_section(section)

            except Exception as e:
                logger.warning("During solving section, error occured. Skipping it")
                logger.debug(traceback.format_exc())

        logger.info(f"Solved course {course.title} successfully")

    def solve_section(self, section: Section) -> NoReturn:
        logger.info(f"Solving section {section.title}...")
        for unit_id in section.units:
            try:
                unit = self.stepik_client.get_unit(unit_id)

                self.solve_unit(unit)

            except Exception as e:
                logger.warning("During solving unit, error occured. Skipping it")
                logger.debug(traceback.format_exc())

        logger.info(f"Solved section {section.title} successfully")

    def solve_unit(self, unit: Unit) -> NoReturn:
        assignments = self.stepik_client.get_assignments(
            ids=unit.assignments,
        )

        lesson = self.stepik_client.get_lesson(unit.lesson)
        logger.info(f"Solving lesson {lesson.title}...")

        steps = self.stepik_client.get_steps(lesson.steps)
        progresses = self.stepik_client.get_progresses(
            ids=[step.progress for step in steps],
        )

        assignment_map = {assignment.step: assignment.id for assignment in assignments}
        assignment_ids = [assignment_map.get(step.id, 0) for step in steps]

        for step, progress, assignment_id in zip(steps, progresses, assignment_ids):
            try:
                self.solve_step(step, progress, assignment_id)

            except Exception as e:
                logger.warning("During solving step, error occured. Skipping it")
                logger.debug(traceback.format_exc())

        logger.info(f"Solved lesson {lesson.title} successfully")


    def solve_step(self, step: Step, progress: Progress, assignment_id: int) -> NoReturn:
        if (not progress.is_passed):
            self.solver.context = []
            logger.info(f"Solving step {step.position}...")
            self.executor.submit(self.solver.solve,
                step=step,
                assignment_id=assignment_id,
                user_id=self.id,
                stepik_client=self.stepik_client,
            )

            logger.info(f"Solved step {step.position} successfully")


