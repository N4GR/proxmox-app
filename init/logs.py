import sys
import logging
from modules import logs

def setup(name: str) -> logging.Logger:
    logging = logs.Logger(name)
    log = logging.log

    sys.excepthook = logging.custom_excepthook

    return log