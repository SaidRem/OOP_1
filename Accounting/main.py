from datetime import datetime

from application.db.people import get_employees
from application.get_info import get_info
from application.salary import calculate_salary


def main():
    print(datetime.now())


if __name__ == "__main__":
    main()
    get_employees()
    get_info()
    calculate_salary()
