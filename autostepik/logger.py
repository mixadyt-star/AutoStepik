import logging

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