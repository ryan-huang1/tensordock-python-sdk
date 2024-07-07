import requests
from ..exceptions import TensorDockAPIException

class Billing:
    def __init__(self, api):
        self.api = api

    def get_balance(self):
        url = f"{self.api.base_url}/billing/balance"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error retrieving balance: {response.text}")

    def get_revenue(self, start_timestamp=None, end_timestamp=None, hostnode_id=None):
        url = f"{self.api.base_url}/billing/revenue"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'start_timestamp': start_timestamp,
            'end_timestamp': end_timestamp,
            'hostnode_id': hostnode_id
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error retrieving revenue: {response.text}")

    def get_monthly_summary(self, period):
        url = f"{self.api.base_url}/billing/summary"
        data = {
            'api_key': self.api.api_key,
            'api_token': self.api.api_token,
            'period': period
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error retrieving monthly summary: {response.text}")

# tensordock/exceptions.py
class TensorDockAPIException(Exception):
    pass
