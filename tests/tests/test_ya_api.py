import os
import time
import pytest
from dotenv import load_dotenv
from yandexDiskAPI import YandexDiskAPI

load_dotenv()
TOKEN = os.getenv("APITOKEN")

UNIQUE_FOLDER_NAME = f"test_folder_{int(time.time())}"


@pytest.fixture(scope="module")
def yandex_api():
    if not TOKEN:
        pytest.fail("APITOKEN is not set in the .env file")
    return YandexDiskAPI(TOKEN)


def test_get_files_list_real(yandex_api):
    response = yandex_api.get_files_list()
    assert response.status_code == 200
    assert "items" in response.json()


def test_create_folder_real(yandex_api):
    response = yandex_api.create_folder(UNIQUE_FOLDER_NAME)
    assert response.status_code in (201, 409)  # 201 = Created, 409 = Already exists


def test_check_folder_exists_real(yandex_api):
    yandex_api.create_folder(UNIQUE_FOLDER_NAME)

    exists = yandex_api.check_folder_exists(UNIQUE_FOLDER_NAME)
    assert exists is True


def test_create_invalid_folder_name(yandex_api):
    response = yandex_api.create_folder("///////invalid///")
    assert response.status_code in (400, 404)  # Bad Request
