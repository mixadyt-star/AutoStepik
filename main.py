from autostepik.autostepik import AutoStepik
from autostepik.solvers import AiSolver, OpenRouterClient
from autostepik.logger import logger

solver = AiSolver(
    ai_client=OpenRouterClient(
        token="YOUR OPEN ROUTER TOKEN",
        model="YOUR MODEL NAME" # You can find them on https://openrouter.ai/models
    ),
)

try:
    AutoStepik(
        email="YOUR EMAIL",
        password="YOUR PASSWORD",
        solver=solver,
        max_workers=2,
    ).solve()

except KeyboardInterrupt:
    logger.info("See you next time! ^_~")
