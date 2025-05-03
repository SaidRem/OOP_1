import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

APITOKEN = os.getenv("APITOKEN")


class YandexDiskAPI:
    def __init__(self, oauth_token):
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {'Authorization': f'OAuth {oauth_token}'}

    def get_files_list(self):
        return requests.get(
            f"{self.base_url}/resources/files",
            headers=self.headers
        )

    def create_folder(self, folder_name):
        return requests.put(
            f"{self.base_url}/resources",
            params={'path': f'disk:/{folder_name}'},
            headers=self.headers
        )

    def check_folder_exists(self, folder_name):
        response = requests.get(
            f"{self.base_url}/resources",
            params={'path': f'disk:/{folder_name}'},
            headers=self.headers
        )
        return response.status_code == 200


if __name__ == "__main__":
    obj = YandexDiskAPI(APITOKEN)
    # print(obj.create_folder("TEST___"))
    print(obj.get_files_list().json())
