from .base import CodeSolver, ChoiceSolver, StringSolver, TextSolver, SortingSolver
from ..logger import logger
from time import sleep
import json
from .ai_client import AiClient
from .prompt_generator import PromptGenerator, DefaultPromptGenerator
from typing import Optional

class AiSolver(CodeSolver, ChoiceSolver, TextSolver, StringSolver, SortingSolver):
    def __init__(self, ai_client: AiClient, prompt_generator: Optional[PromptGenerator] = None):
        self.ai_client = ai_client
        self.prompt_generator = prompt_generator or DefaultPromptGenerator()

    def solve(self, step, assignment_id, user_id, stepik_client):
        logger.info(f"Solving {step.block.name} task...")

        match step.block.name:
            case "code":
                new_attempt = stepik_client.create_new_attempt(step_id=step.id)

                prompt = self.prompt_generator.generate_code_prompt(
                    step=step,
                    attempt=new_attempt,
                )
                
                code = self.ai_client.get_response(prompt).replace("```python", "").replace("```", "")

                self.send_code(
                    attempt_id=new_attempt.id,
                    code=code,
                    stepik_client=stepik_client,
                )
        
            case "choice":
                new_attempt = stepik_client.create_new_attempt(step_id=step.id)
                
                prompt = self.prompt_generator.generate_choice_prompt(
                    step=step,
                    attempt=new_attempt,
                )

                response = self.ai_client.get_response(prompt)
                choices = json.loads(response.replace("```json", "").replace("```", ""))

                self.send_choices(
                    attempt_id=new_attempt.id,
                    choices=choices,
                    stepik_client=stepik_client,
                )

            case "text" | "video":
                self.send_text(step_id=step.id, assignment_id=assignment_id, stepik_client=stepik_client)

                return

            case "string":
                new_attempt = stepik_client.create_new_attempt(step_id=step.id)
                
                prompt = self.prompt_generator.generate_string_prompt(
                    step=step,
                    attempt=new_attempt,
                )

                text = self.ai_client.get_response(prompt)

                self.send_string(
                    attempt_id=new_attempt.id,
                    text=text,
                    stepik_client=stepik_client,
                )

            case "sorting":
                new_attempt = stepik_client.create_new_attempt(step_id=step.id)
                
                prompt = self.prompt_generator.generate_sorting_prompt(
                    step=step,
                    attempt=new_attempt,
                )

                response = self.ai_client.get_response(prompt)  
                ordering = json.loads(response)

                self.send_ordering(
                    attempt_id=new_attempt.id,
                    ordering=ordering,
                    stepik_client=stepik_client,
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