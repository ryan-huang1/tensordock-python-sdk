import requests
from ..exceptions import TensorDockAPIException

class Servers:
    def __init__(self, api):
        self.api = api

    def get_available_servers(self):
        url = f"{self.api.base_url}/available_servers"
        params = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error getting available servers: {response.text}")

    def get_available_hostnodes(self):
        url = f"{self.api.base_url}/available_hostnodes"
        params = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error getting available hostnodes: {response.text}")

    def get_hostnode_details(self, hostnode_id):
        url = f"{self.api.base_url}/hostnode_details"
        params = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'hostnode_id': hostnode_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error getting hostnode details: {response.text}")
