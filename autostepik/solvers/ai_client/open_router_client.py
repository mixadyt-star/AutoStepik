from .ai_client import AiClient
from ...logger import logger
import requests
import traceback
import json
from typing import Optional

class OpenRouterClient(AiClient):
    def __init__(self, token: str, model: Optional[str] = "kwaipilot/kat-coder-pro:free"):
        self.token = token
        self.model = model

    def get_response(self, prompt):
        logger.info(f"Sending task to AI...")

        while True:
            try:
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.token}",
                        "Content-Type": "application/json",
                    },
                    data=json.dumps({
                        "model": self.model,
                        "messages": [
                            {
                            "role": "user",
                            "content": prompt
                            }
                        ]
                    })
                )
            
                response = response.json()
                response = response["choices"][0]["message"]["content"]

                logger.info(f"Got response from AI")

                return response

            except Exception as e:
                logger.warning("During receiving response from open router, error occured. Trying again")
                logger.debug(traceback.format_exc())