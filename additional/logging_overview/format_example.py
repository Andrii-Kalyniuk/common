import logging

"""

The log message
Severity of the log message
Timestamp at which the message was logged
Name of the module where the event occured
Line number of the module that registered the log

"""

log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
             "%(filename)s::%(lineno)d::%(message)s"


logging.basicConfig(level='DEBUG', format=log_format)
logging.debug("This is a debug message")
logging.info("This is an informational message")
logging.warning("Careful! Something does not look right")
logging.error("You have encountered an error")
logging.critical("You are in trouble")