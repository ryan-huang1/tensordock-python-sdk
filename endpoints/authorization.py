import requests
from ..exceptions import TensorDockAPIException

class Authorization:
    def __init__(self, api):
        self.api = api

    def test_authorization(self):
        url = f"{self.api.base_url}/test_authorization"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error testing authorization: {response.text}")

    def list_authorizations(self):
        url = f"{self.api.base_url}/authorizations_list"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error listing authorizations: {response.text}")
