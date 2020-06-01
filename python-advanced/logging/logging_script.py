import logging

logging.basicConfig(
  filename = 'app.log',
  filemode = 'w',
  format = '%(name)s - %(levelname)s - %(message)s'
)

logging.warning('This warning message is logged to a file')
