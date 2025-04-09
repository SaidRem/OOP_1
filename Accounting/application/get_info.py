import requests
import logging

logger = logging.getLogger(__name__)
logger.info("Info message from get_info.py")
print("Info message from get_info.py")


def get_info():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    logger.info(r.status_code)
    result = r.json
    logger.info(result)
    print(result)
    return result


if __name__ == '__main__':
    logger.info(get_info())
