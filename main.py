from autostepik.autostepik import AutoStepik
from autostepik.solvers import DefaultSolver

solver = DefaultSolver(token_list=[
    "YOUR OPEN ROUTER TOKEN"
])

auto = AutoStepik(
    email="YOUR EMAIL",
    password="YOUR PASSWORD",
    solver=solver,
)

auto.solve()