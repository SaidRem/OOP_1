import pytest
from unittest.mock import patch
from dotenv import load_dotenv
from yandexDiskAPI import YandexDiskAPI


@pytest.fixture
def yandex_api():
    return YandexDiskAPI("fake_token")


@patch("yandexDiskAPI.requests.get")
def test_get_files_list(mock_get, yandex_api):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}

    response = yandex_api.get_files_list()
    assert response.status_code == 200
    assert response.json() == {"items": []}


@patch("yandexDiskAPI.requests.put")
def test_create_folder(mock_put, yandex_api):
    mock_response = mock_put.return_value
    mock_response.status_code = 201

    response = yandex_api.create_folder("NewFolder")
    assert response.status_code == 201
    mock_put.assert_called_once()


@patch("yandexDiskAPI.requests.get")
def test_check_folder_exists_true(mock_get, yandex_api):
    mock_get.return_value.status_code = 200
    assert yandex_api.check_folder_exists("ExistingFolder") is True


@patch("yandexDiskAPI.requests.get")
def test_check_folder_exists_false(mock_get, yandex_api):
    mock_get.return_value.status_code = 404
    assert yandex_api.check_folder_exists("NonexistentFolder") is False

# ---------- Negative Tests ----------


@patch("yandexDiskAPI.requests.get")
def test_get_files_list_invalid_token(mock_get, yandex_api):
    mock_get.return_value.status_code = 401
    response = yandex_api.get_files_list()
    assert response.status_code == 401


@patch("yandexDiskAPI.requests.put")
def test_create_existing_folder(mock_put, yandex_api):
    mock_put.return_value.status_code = 409  # Conflict
    response = yandex_api.create_folder("ExistingFolder")
    assert response.status_code == 409


@patch("yandexDiskAPI.requests.put")
def test_create_invalid_folder_name(mock_put, yandex_api):
    mock_put.return_value.status_code = 400  # Bad Request
    response = yandex_api.create_folder("///invalid///name")
    assert response.status_code == 400
