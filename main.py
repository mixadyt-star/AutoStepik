from autostepik.autostepik import AutoStepik
from autostepik.solvers import DefaultSolver
from autostepik.logger import logger

solver = DefaultSolver(token_list=[
    "YOUR OPEN ROUTER TOKEN"
])

try:
    AutoStepik(
        email="YOUR EMAIL",
        password="YOUR PASSWORD",
        solver=solver,
    ).solve()

except KeyboardInterrupt:
    logger.info("See you next time! ^_~")