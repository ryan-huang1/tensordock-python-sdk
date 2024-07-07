import requests
from ..exceptions import TensorDockAPIException

class Authorization:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None):
        """
        Internal method to make API requests.
        """
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
        """
        Test if the provided API key and token are valid.

        Returns:
            dict: A dictionary containing the success status.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('test')

    def list_authorizations(self):
        """
        Retrieve a list of all authorizations for the organization.

        Returns:
            dict: A dictionary containing the success status and a list of authorizations.

        Example response:
            {
                "success": true,
                "authorizations": {
                    "test_auth": {
                        "permissions": "All",
                        "timestamp_creation": "2022-12-04 02:26:01.898472",
                        "note": "Use for testing purposes"
                    },
                    "perm_auth": {
                        "permissions": "All",
                        "timestamp_creation": "2022-12-03 03:43:07.125862",
                        "note": "Permanent use cases"
                    }
                }
            }
        """
        return self._make_request('list')
