from .solver import Solver
from ..logger import logger
from time import sleep
import json
from .ai_client import AiClient
from .prompt_generator import PromptGenerator, DefaultPromptGenerator
from typing import Optional

class AiSolver(Solver):
    def __init__(self, ai_client: AiClient, prompt_generator: Optional[PromptGenerator] = None):
        self.supported = [
            "text",
            "video",
            "code",
            "choice",
            "string",
            "sorting",
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
            
            response = self.ai_client.get_response(prompt)

        match step.block.name:
            case "code":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    code=response,
                )
        
            case "choice":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    choices=json.loads(response),
                )

            case "string":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    text=response,
                )

            case "sorting":
                stepik_client.create_new_solution(
                    attempt_id=new_attempt.id,
                    ordering=json.loads(response),
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
                    break

                case "correct":
                    logger.info(f"Correct solution!")
                    break

                case "evaluation":
                    logger.info("Evaluation status...")