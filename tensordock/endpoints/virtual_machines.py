import requests
from ..exceptions import TensorDockAPIException

class VirtualMachines:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None, method='post'):
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
        return self._make_request(f'deploy/hostnodes?minGPUCount={min_gpu_count}', method='get')

    def get_hostnode_details(self, hostnode_uuid):
        return self._make_request(f'deploy/hostnodes/{hostnode_uuid}', method='get')

    def deploy_vm(self, **kwargs):
        return self._make_request('deploy/single', kwargs)

    def validate_spot_price_new(self, **kwargs):
        return self._make_request('spot/validate/new', kwargs)

    def validate_spot_price_existing(self, server, price):
        return self._make_request('spot/validate/existing', {'server': server, 'price': price})

    def list_vms(self):
        return self._make_request('list')

    def get_vm_details(self, server):
        return self._make_request('get/single', {'server': server})

    def start_vm(self, server):
        return self._make_request('start/single', {'server': server})

    def stop_vm(self, server, disassociate_resources=False):
        return self._make_request('stop/single', {'server': server, 'disassociate_resources': disassociate_resources})

    def modify_vm(self, server_id, **kwargs):
        kwargs['server_id'] = server_id
        return self._make_request('modify/single', kwargs)

    def delete_vm(self, server):
        return self._make_request('delete/single', {'server': server})