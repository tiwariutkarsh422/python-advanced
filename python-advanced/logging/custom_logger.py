import logging

logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file_log.log')

c_handler.setLevel(logging.WARNING) #logging level less than WARNING will not be printed on console
f_handler.setLevel(logging.ERROR)  #logging level less than ERROR will not be printed on console

c_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_formatter)
f_handler.setFormatter(f_formatter)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning message.')
logger.error('This is an error message.')

