from .solver import Solver
from ..logger import logger
from time import sleep
import json
from .ai_client import AiClient
from .prompt_generator import PromptGenerator, DefaultPromptGenerator
from typing import Optional

class AiSolver(Solver):
    def __init__(self, ai_client: AiClient, prompt_generator: Optional[PromptGenerator] = None):
        self.correct = 0
        self.wrong = 0

        self.supported = [
            "text",
            "video",
            "code",
            "choice",
            "string",
            "sorting",
            "matching",
            "fill-blanks",
            "number",
            "table",
        ]

        self.ai_client = ai_client
        self.prompt_generator = prompt_generator or DefaultPromptGenerator()

    def solve(self, step, assignment_id, user_id, stepik_client):
        logger.info(f"Solving {step.block.name} task...")

        if (step.block.name == "text" or step.block.name == "video"):
            stepik_client.set_view(
                step_id=step.id,
                assignment_id=assignment_id,
            )

            return

        if (step.block.name in self.supported):
            new_attempt = stepik_client.create_new_attempt(step_id=step.id)

            prompt = self.prompt_generator.generate_prompt(
                step=step,
                attempt=new_attempt,
                task_type=step.block.name,
            )
            
            answer = self.ai_client.get_answer(prompt)

        match step.block.name:
            case "code":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    code=answer,
                )
        
            case "choice" | "table":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    choices=json.loads(answer),
                )

            case "string":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    text=answer,
                )

            case "sorting" | "matching":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    ordering=json.loads(answer),
                )

            case "fill-blanks":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    blanks=json.loads(answer),
                )

            case "number":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    number=answer,
                )
                    
            case _:
                logger.warning(f"Unknown task type: {step.block.name}, skipping it")
                return
        
        logger.info("Sent answer to stepik server successfully")

        while (True):
            sleep(1)

            submissions = stepik_client.get_submissions(
                limit=1,
                step_id=step.id,
                user_id=user_id,
            )

            match submissions[0].status:
                case "wrong":
                    logger.info(f"Wrong solution :(")
                    self.wrong += 1
                    break

                case "correct":
                    logger.info(f"Correct solution!")
                    self.correct += 1
                    break

                case "evaluation":
                    logger.info("Evaluation status...")

        logger.info(f"✅ Correct solutions: {self.correct} ❌ Wrong solutions: {self.wrong}")