import requests
from ..exceptions import TensorDockAPIException

class Billing:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None):
        url = f"{self.api.base_url}/billing/{endpoint}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = data or {}
        data['api_key'] = self.api.api_key
        data['api_token'] = self.api.api_token
        
        response = requests.post(url, data=data, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise TensorDockAPIException(f"Error in billing/{endpoint}: {response.text}")

    def get_balance(self):
        return self._make_request('balance')

    def get_revenue(self, start_timestamp=None, end_timestamp=None, hostnode_id=None):
        data = {
            'start_timestamp': start_timestamp,
            'end_timestamp': end_timestamp,
            'hostnode_id': hostnode_id
        }
        return self._make_request('revenue', {k: v for k, v in data.items() if v is not None})

    def get_monthly_summary(self, period):
        return self._make_request('summary', {'period': period})