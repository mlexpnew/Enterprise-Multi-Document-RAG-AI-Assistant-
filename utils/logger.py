from loguru import logger

from config.settings import LOG_FOLDER

logger.remove()

logger.add(
    LOG_FOLDER / "rag.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    enqueue=True,
)

logger.add(
    lambda msg: print(msg, end=""),
    level="INFO",
)

log = logger