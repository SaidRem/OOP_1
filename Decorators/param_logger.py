import os
import logging
from functools import wraps


loggers_cache = {}


def logger(path: str, write_mode: str = "a"):
    """
    Decorator to log function calls into the given log file.

    Args:
        path (str): Path to the log file.
        write_mode (str, optional): File write mode. Default to "a" (append).

    Returns:
        function: A decorator that wraps the original function with logging.
    """

    def __logger(old_function):
        # Create or resuse logger for the file path.
        abs_path = os.path.abspath(path)
        if abs_path not in loggers_cache:
            func_logger = logging.getLogger(f"decorated.{abs_path}")
            func_logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(message)s",
                datefmt="%d-%m-%Y %H:%M:%S"
            )
            # Console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            func_logger.addHandler(ch)

            # File handler.
            file_handler = logging.FileHandler(path, mode=write_mode)
            file_handler.setFormatter(formatter)
            func_logger.addHandler(file_handler)

            # Save this logger for the path
            loggers_cache[abs_path] = func_logger
        else:
            func_logger = loggers_cache[abs_path]

        @wraps(old_function)
        def new_function(*args, **kwargs):
            try:
                result = old_function(*args, **kwargs)
                func_logger.info(
                    f"func {old_function.__name__} run with {args = } and {kwargs = } | {result = }"
                )
                return result
            except Exception as err:
                func_logger.exception(
                    f"func {old_function.__name__} raised {err.__class__.__name__} with {args!r} and {kwargs!r}"
                )
                raise

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
