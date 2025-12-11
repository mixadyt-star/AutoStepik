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
        if (step.block.name == "code"):
            logger.info(f"Solving code task...")

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

            logger.info(f"Sent code to stepik server successfully")

            while (True):
                sleep(1)

                submissions = stepik_client.get_submissions(
                        limit=1,
                        step_id=step.id,
                        user_id=user_id,
                )

                if (submissions[0].status == "wrong"):
                    logger.info(f"Wrong solution :(")
                    break
                        
                elif (submissions[0].status == "evaluation"):
                    logger.info("Evaluation status...")

                else:
                    logger.info(f"Correct solution! (status {submissions[0].status})")
                    break
        
        elif (step.block.name == "choice"):
            logger.info(f"Solving choice task...")

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

            logger.info(f"Sent choices to stepik server successfully")

            while (True):
                sleep(1)

                submissions = stepik_client.get_submissions(
                        limit=1,
                        step_id=step.id,
                        user_id=user_id,
                )

                if (submissions[0].status == "wrong"):
                    logger.info(f"Wrong solution :(")
                    break
                        
                elif (submissions[0].status == "evaluation"):
                    logger.info("Evaluation status...")

                else:
                    logger.info(f"Correct solution! (status {submissions[0].status})")
                    break

        elif (step.block.name == "text" or step.block.name == "video"):
            logger.info(f"Solving {step.block.name} task...")
            self.send_text(step_id=step.id, assignment_id=assignment_id, stepik_client=stepik_client)

        elif (step.block.name == "string"):
            logger.info(f"Solving string task...")

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

            logger.info(f"Sent answer to stepik server successfully")

            while (True):
                sleep(1)

                submissions = stepik_client.get_submissions(
                        limit=1,
                        step_id=step.id,
                        user_id=user_id,
                )

                if (submissions[0].status == "wrong"):
                    logger.info(f"Wrong solution :(")
                    break
                        
                elif (submissions[0].status == "evaluation"):
                    logger.info("Evaluation status...")

                else:
                    logger.info(f"Correct solution! (status {submissions[0].status})")
                    break

        elif (step.block.name == "sorting"):
            logger.info(f"Solving sorting task...")

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

            logger.info(f"Sent ordering to stepik server successfully")

            while (True):
                sleep(1)

                submissions = stepik_client.get_submissions(
                        limit=1,
                        step_id=step.id,
                        user_id=user_id,
                )

                if (submissions[0].status == "wrong"):
                    logger.info(f"Wrong solution :(")
                    break
                        
                elif (submissions[0].status == "evaluation"):
                    logger.info("Evaluation status...")

                else:
                    logger.info(f"Correct solution! (status {submissions[0].status})")
                    break
                    
        else:
            logger.warning(f"Unknown task type: {step.block.name}, skipping it")