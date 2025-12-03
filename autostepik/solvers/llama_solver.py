from .base import CodeSolver, ChoiceSolver, TextSolver
from ..logger import logger
from time import sleep
import requests
import json
from typing import List

class LlamaSolver(CodeSolver, ChoiceSolver, TextSolver):
    def __init__(self, token_list: List[str]):
        self.token_list = token_list

    def solve(self, step, assignment_id, user_id, stepik_client):
        if (step.block.name == "code"):
            logger.info(f"Solving code task...")

            new_attempt = stepik_client.create_new_attempt(step_id=step.id)
            
            prompt = """
            Сейчас я дам тебе условие задачи на программирование.
            Тебе нужно написать код, который эту задачу решит.
            В ответ напиши ТОЛЬКО код решения ОБЫЧНЫМ ТЕКСТОМ БЕЗ МАРКДАУНА и НИЧЕГО больше.
            """ + step.block.text + "\nТакже вот дополнительная информация о задаче: " + str(step.block.options)

            logger.info(f"Sending task to AI...")
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.token_list[0]}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": "kwaipilot/kat-coder-pro:free", # "x-ai/grok-4.1-fast:free",
                    "messages": [
                        {
                        "role": "user",
                        "content": prompt
                        }
                    ]
                })
            )

            response = response.json()
            response = response['choices'][0]['message']

            logger.info(f"Got response from AI")
            
            code = response["content"].replace("```python", "").replace("```", "")

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
            
            prompt = """
            Сейчас я дам тебе условие задачи на выбор.
            Тебе нужно выбрать верные по твоему мнению варианты ответа.
            В ответ ОБЯЗАТЕЛЬНО напиши ТОЛЬКО json вида: [false, true, true, false] (ИСПОЛЬЗУЙ ИСКЛЮЧИТЕЛЬНО true и false БЕЗ кавычек) и НИЧЕГО БОЛЬШЕ.
            Ещё ты ОБЯЗЯАТЕЛЬНО должен заполнить все опции значениями true / false, т.е. например если значения два и 1 верно ты должен вернуть [true, false].
            Перед отправкой перевроверь формат ответа.
            """ + step.block.text + "\nВот опции ответа: " + str(new_attempt.dataset) + "\nТакже вот дополнительная информация о задаче: " + str(step.block.options)

            logger.info(f"Sending task to AI...")
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.token_list[0]}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": "kwaipilot/kat-coder-pro:free", # "x-ai/grok-4.1-fast:free",
                    "messages": [
                        {
                        "role": "user",
                        "content": prompt
                        }
                    ],
                })
            )

            response = response.json()
            response = response['choices'][0]['message']

            logger.info(f"Got response from AI")
            
            choices = json.loads(response["content"])

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

        elif (step.block.name == "text"):
            logger.info(f"Solving text task...")
            self.send_text(step_id=step.id, assignment_id=assignment_id, stepik_client=stepik_client)