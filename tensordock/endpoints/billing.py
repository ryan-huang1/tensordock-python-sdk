import requests
from ..exceptions import TensorDockAPIException

class Billing:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None):
        """
        Internal method to make API requests.
        """
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
        """
        Retrieve the current balance and hourly cost for the organization.

        Returns:
            dict: A dictionary containing the success status, balance, and hourly cost.

        Example response:
            {
                "balance": 999.987,
                "hourly_cost": 0.856,
                "success": true
            }
        """
        return self._make_request('balance')

    def get_revenue(self, start_timestamp=None, end_timestamp=None, hostnode_id=None):
        """
        Retrieve revenue information for hosting providers.

        Args:
            start_timestamp (str, optional): Start timestamp of the period to retrieve historical data for.
            end_timestamp (str, optional): End timestamp of the period to retrieve historical data for.
            hostnode_id (str, optional): Hostnode to filter data by.

        Returns:
            dict: A dictionary containing revenue data for each hostnode.

        Example response:
            {
                "data": [
                    {
                        "hostnode_id": "7d3a07b6-de25-44a2-a9f4-1cd241fa0d0f",
                        "location": "Chicago, Illinois, United States",
                        "used_storage": 30,
                        "used_gpus": 3,
                        "used_cpus": 2,
                        "used_ram": 10,
                        "available_storage": 170,
                        "available_gpus": 1,
                        "available_cpus": 3,
                        "available_ram": 50,
                        "revenue_storage": 0.03,
                        "revenue_compute": 1.03,
                        "virtual_machines": [
                            {
                                "id": "f2467993-1f6b-43b2-8744-7b14dfc0bdab",
                                "used_storage": 20,
                                "used_gpus": 1,
                                "used_cpus": 1,
                                "used_ram": 5,
                                "revenue_storage": 0.03,
                                "revenue_compute": 1.03
                            }
                        ]
                    }
                ]
            }
        """
        data = {
            'start_timestamp': start_timestamp,
            'end_timestamp': end_timestamp,
            'hostnode_id': hostnode_id
        }
        return self._make_request('revenue', {k: v for k, v in data.items() if v is not None})

    def get_monthly_summary(self, period):
        """
        Retrieve a monthly summary of billing information.

        Args:
            period (str): Billing period to retrieve transactions for, in the format YYYY-MM (e.g., "2024-01").

        Returns:
            dict: A dictionary containing the monthly billing summary.

        Example response:
            {
                "bill_period": {
                    "endM": "03",
                    "endY": "2024",
                    "startM": "02",
                    "startY": "2024"
                },
                "changes": {
                    "expenses": "332.15",
                    "payouts": "9304.01"
                },
                "final_balance": "929.41",
                "organization_billing_address": null,
                "organization_tax_id": "37-3294571",
                "previous_balance": "1765.06",
                "transactions": {
                    "deposits": [],
                    "storage_expenses": [],
                    "storage_payouts": [
                        {
                            "billing_period_end": "03/01",
                            "billing_period_start": "02/01",
                            "hostnode_id": "2f0b8e32-b3e9-44ca-b3ca-8afa4c1320bf",
                            "rate_hourly": 0.01,
                            "storage_amount": 200,
                            "total_amount": 5.42,
                            "virtual_machine_id": "d7e95e9c-9af2-43b0-a413-1141c97a9cc9"
                        }
                    ],
                    "vm_expenses": [],
                    "vm_payouts": [
                        {
                            "billing_period_end": "03/01",
                            "billing_period_start": "02/01",
                            "gpu_details": "1x L40 48 GB",
                            "hostnode_id": "2f0b8e32-b3e9-44ca-b3ca-8afa4c1320bf",
                            "rate_hourly": 1.56,
                            "total_amount": 544.312,
                            "virtual_machine_id": "d7e95e9c-9af2-43b0-a413-1141c97a9cc9"
                        }
                    ],
                    "withdrawals": []
                }
            }
        """
        return self._make_request('summary', {'period': period})
