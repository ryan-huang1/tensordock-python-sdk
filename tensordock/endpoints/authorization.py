import requests
from ..exceptions import TensorDockAPIException

class Authorization:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None):
        url = f"{self.api.base_url}/auth/{endpoint}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = data or {}
        data['api_key'] = self.api.api_key
        data['api_token'] = self.api.api_token
        
        response = requests.post(url, data=data, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error in auth/{endpoint}: {response.text}")

    def test_authorization(self):
        return self._make_request('test')

    def list_authorizations(self):
        return self._make_request('list')