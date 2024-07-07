import requests
from ..exceptions import TensorDockAPIException

class Containers:
    def __init__(self, api):
        self.api = api

    def deploy_container(self, **kwargs):
        url = f"{self.api.base_url}/deploy_container"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            **kwargs
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error deploying container: {response.text}")

    def scale_container(self, container_id, replicas):
        url = f"{self.api.base_url}/scale_container"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'container_id': container_id,
            'replicas': replicas
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error scaling container: {response.text}")

    def terminate_container(self, container_id):
        url = f"{self.api.base_url}/terminate_container"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'container_id': container_id
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error terminating container: {response.text}")

    def get_container_replicas(self, container_id):
        url = f"{self.api.base_url}/container_replicas"
        params = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'container_id': container_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error getting container replicas: {response.text}")
