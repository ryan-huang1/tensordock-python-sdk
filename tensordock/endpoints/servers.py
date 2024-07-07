import requests
from ..exceptions import TensorDockAPIException

class Servers:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None, method='get'):
        url = f"{self.api.base_url}/client/{endpoint}"
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
            raise TensorDockAPIException(f"Error in client/{endpoint}: {response.text}")

    def get_available_hostnodes(self, min_gpu_count=0):
        return self._make_request(f'deploy/hostnodes?minGPUCount={min_gpu_count}')

    def get_hostnode_details(self, hostnode_uuid):
        return self._make_request(f'deploy/hostnodes/{hostnode_uuid}')

    def list_servers(self):
        return self._make_request('list')

    def get_server_details(self, server_id):
        return self._make_request('get/single', {'server': server_id}, method='post')