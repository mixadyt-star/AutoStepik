from autostepik.autostepik import AutoStepik
from autostepik.solvers import AiSolver, OpenRouterClient
from autostepik.logger import logger

solver = AiSolver(
    ai_client=OpenRouterClient(
        token="YOUR OPEN ROUTER TOKEN",
        model="mistralai/devstral-2512:free",
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