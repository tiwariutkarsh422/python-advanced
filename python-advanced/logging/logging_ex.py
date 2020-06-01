import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

'''Alternative to logging.error can be exception method '''
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")
