from us_visa.logger import logging
from us_visa.exception import USvisaException


logging.info("Demo file for MongoDB operations")

try:
    a = 1 / 0
except Exception as e:
    raise USvisaException(e, sys)