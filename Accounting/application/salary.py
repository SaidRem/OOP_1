import logging


logger = logging.getLogger(__name__)
logger.info("This is an info message from salary.py")
print("This is an info message from salary.py")


def calculate_salary():
    logger.info("Here we calculate salary in 'calculate_salary()'")
    print("Here we calculate salary in 'calculate_salary()'")
