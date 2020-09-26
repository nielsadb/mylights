import logging
from sys import stderr

def _make_logger():
  handler = logging.StreamHandler(stderr)
  formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
  handler.setFormatter(formatter)
  log = logging.getLogger('mylights')
  log.addHandler(handler)
  log.setLevel(logging.INFO)
  return log

_log = _make_logger()

class MyLightException(BaseException):
  def __init__(self, msg):
    self._msg = msg

def get_logger(caller):
  return _log
