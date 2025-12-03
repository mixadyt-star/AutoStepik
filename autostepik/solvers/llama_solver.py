from .base import CodeSolver, ChoiceSolver, TextSolver
from time import sleep
import logging
import requests
import json
from typing import List

RESET = "\033[0m"
INVERSE = "\033[7m"
GREEN = "\033[32m"
RED_BG = "\033[41m"

logging.basicConfig(
    level=logging.INFO,
    format=f"{GREEN}[ %(asctime)s %(filename)s:%(lineno)d %(levelname)s] %(message)s{RESET}",
    datefmt="%y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)

class LlamaSolver(CodeSolver, ChoiceSolver, TextSolver):
    def __init__(self, token_list: List[str]):
        self.token_list = token_list

    def solve(self, step, assignment_id, user_id, stepik_client):
        if (step.block.name == "code"):
            logging.info(f"Solving code task...")

            new_attempt = stepik_client.create_new_attempt(step_id=step.id)
            
            prompt = """
            Сейчас я дам тебе условие задачи на программирование.
            Тебе нужно написать код, который эту задачу решит.
            В ответ напиши ТОЛЬКО код решения ОБЫЧНЫМ ТЕКСТОМ БЕЗ МАРКДАУНА и НИЧЕГО больше.
            """ + step.block.text + "\nТакже вот дополнительная информация о задаче: " + str(step.block.options)

            logging.info(f"Sending task to AI...")
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

            logging.info(f"Got response from AI")
            
            code = response["content"].replace("```python", "").replace("```", "")

            self.send_code(
                attempt_id=new_attempt.id,
                code=code,
                stepik_client=stepik_client,
            )

            logging.info(f"Sent code to stepik server successfully")

            while (True):
                sleep(1)

                submissions = stepik_client.get_submissions(
                        limit=1,
                        step_id=step.id,
                        user_id=user_id,
                )

                if (submissions[0].status == "wrong"):
                    logging.info(f"Wrong solution :(")
                    break
                        
                elif (submissions[0].status == "evaluation"):
                    logging.info("Evaluation status...")

                else:
                    logging.info(f"Correct solution! (status {submissions[0].status})")
                    break
        
        elif (step.block.name == "choice"):
            logging.info(f"Solving choice task...")

            new_attempt = stepik_client.create_new_attempt(step_id=step.id)
            
            prompt = """
            Сейчас я дам тебе условие задачи на выбор.
            Тебе нужно выбрать верные по твоему мнению варианты ответа.
            В ответ ОБЯЗАТЕЛЬНО напиши ТОЛЬКО json вида: [false, true, true, false] (ИСПОЛЬЗУЙ ИСКЛЮЧИТЕЛЬНО true и false БЕЗ кавычек) и НИЧЕГО БОЛЬШЕ.
            Ещё ты ОБЯЗЯАТЕЛЬНО должен заполнить все опции значениями true / false, т.е. например если значения два и 1 верно ты должен вернуть [true, false].
            Перед отправкой перевроверь формат ответа.
            """ + step.block.text + "\nВот опции ответа: " + str(new_attempt.dataset) + "\nТакже вот дополнительная информация о задаче: " + str(step.block.options)

            logging.info(f"Sending task to AI...")
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

            logging.info(f"Got response from AI")
            
            choices = json.loads(response["content"])

            self.send_choices(
                attempt_id=new_attempt.id,
                choices=choices,
                stepik_client=stepik_client,
            )

            logging.info(f"Sent choices to stepik server successfully")

            while (True):
                sleep(1)

                submissions = stepik_client.get_submissions(
                        limit=1,
                        step_id=step.id,
                        user_id=user_id,
                )

                if (submissions[0].status == "wrong"):
                    logging.info(f"Wrong solution :(")
                    break
                        
                elif (submissions[0].status == "evaluation"):
                    logging.info("Evaluation status...")

                else:
                    logging.info(f"Correct solution! (status {submissions[0].status})")
                    break

        elif (step.block.name == "text"):
            logging.info(f"Solving text task...")
            self.send_text(step_id=step.id, assignment_id=assignment_id, stepik_client=stepik_client)