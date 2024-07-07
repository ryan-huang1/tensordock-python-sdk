import requests
from ..exceptions import TensorDockAPIException

class VirtualMachines:
    def __init__(self, api):
        self.api = api

    def deploy_vm(self, **kwargs):
        url = f"{self.api.base_url}/deploy_vm"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            **kwargs
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error deploying VM: {response.text}")

    def validate_spot_price_new(self, **kwargs):
        url = f"{self.api.base_url}/validate_spot_price_new"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            **kwargs
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error validating spot price for new instance: {response.text}")

    def validate_spot_price_existing(self, **kwargs):
        url = f"{self.api.base_url}/validate_spot_price_existing"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            **kwargs
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error validating spot price for existing instance: {response.text}")

    def list_vms(self):
        url = f"{self.api.base_url}/list_vms"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error listing VMs: {response.text}")

    def get_vm_details(self, vm_id):
        url = f"{self.api.base_url}/vm_details"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'vm_id': vm_id
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error getting VM details: {response.text}")

    def start_vm(self, vm_id):
        url = f"{self.api.base_url}/start_vm"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'vm_id': vm_id
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error starting VM: {response.text}")

    def stop_vm(self, vm_id):
        url = f"{self.api.base_url}/stop_vm"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'vm_id': vm_id
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error stopping VM: {response.text}")

    def modify_vm(self, vm_id, **kwargs):
        url = f"{self.api.base_url}/modify_vm"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'vm_id': vm_id,
            **kwargs
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error modifying VM: {response.text}")

    def delete_vm(self, vm_id):
        url = f"{self.api.base_url}/delete_vm"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'vm_id': vm_id
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error deleting VM: {response.text}")

