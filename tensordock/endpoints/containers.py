import requests
from ..exceptions import TensorDockAPIException

class Containers:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None, method='post'):
        url = f"{self.api.base_url}/client/container/{endpoint}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = data or {}
        data['api_key'] = self.api.api_key
        data['api_token'] = self.api.api_token
        
        if method.lower() == 'get':
            response = requests.get(url, params=data, headers=headers)
        else:
            response = requests.post(url, data=data, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error in client/container/{endpoint}: {response.text}")

    def deploy_container(self, **kwargs):
        return self._make_request('deploy', kwargs)

    def scale_container(self, container_id, replicas):
        return self._make_request('scale', {'container_id': container_id, 'replicas': replicas})

    def stop_container(self, container_id):
        return self._make_request('stop', {'container_id': container_id})

    def get_container_replicas(self, container_id):
        return self._make_request(f'{container_id}/replicas', method='get')