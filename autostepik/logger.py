"""Colorful logger with file write support"""

import logging
import colorlog

logger = colorlog.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.handlers.clear()

console_handler = colorlog.StreamHandler()
console_handler.setFormatter(colorlog.ColoredFormatter(
    fmt="%(log_color)s[%(asctime)s %(filename)s:%(lineno)d %(levelname)s] %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
    style="%",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "bold_light_yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
    reset=True,
))
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('autostepik.log', encoding="utf-8")
file_handler.setFormatter(logging.Formatter(
    fmt="[ %(asctime)s %(filename)s:%(lineno)d %(levelname)s] %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
))
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.propagate = False

if __name__ == "__main__":
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
