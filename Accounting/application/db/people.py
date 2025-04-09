import logging


logger = logging.getLogger(__name__)
logger.info("This is an info message from people.py")

print("This is an info message from people.py")


def get_employees():
    logger.info("Get info about employees from database.")
    print("Get info about employees from database.")
