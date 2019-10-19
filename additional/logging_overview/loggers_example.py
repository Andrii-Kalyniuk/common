import logging

logger = logging.getLogger("loggers_example")
logger.setLevel(logging.DEBUG)

logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.debug("Debug message")
logger.critical("Critical message")
