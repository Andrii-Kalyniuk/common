import logging

logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('our_new_file.log')

f_handler_2 = logging.FileHandler('all_logs.log')

c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
f_handler_2.setLevel(logging.DEBUG)


c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.addHandler(f_handler_2)


logger.debug("This is debug message")
logger.warning('This is a warning')
logger.error('This is an error')

