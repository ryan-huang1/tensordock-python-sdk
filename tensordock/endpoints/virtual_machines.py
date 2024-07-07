import requests
from ..exceptions import TensorDockAPIException

class VirtualMachines:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None, method='post'):
        """
        Internal method to make API requests.
        """
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
        """
        Retrieve a list of available hostnodes.

        Args:
            min_gpu_count (int, optional): Minimum number of GPUs required. Defaults to 0.

        Returns:
            dict: A dictionary containing information about available hostnodes.

        Example response:
            {
                "hostnodes": {
                    "02c65d45-6da5-4232-a8db-ee0e5bc76110": {
                        "location": {
                            "city": "Winnipeg",
                            "country": "Canada",
                            "dc": null,
                            "id": "50cf200c-be1b-4983-a316-369d2eea10ec",
                            "region": "Manitoba"
                        },
                        "networking": {
                            "ports": [20013, 20012, 20011, 20010, 20009],
                            "receive": 1000,
                            "send": 1000
                        },
                        "specs": {
                            "cpu": {
                                "amount": 26,
                                "price": 0.003,
                                "type": "AMD Ryzen 9 5950X"
                            },
                            "gpu": {
                                "geforcertx3080-pcie-10gb": {
                                    "amount": 1,
                                    "price": 0.15
                                }
                            },
                            "ram": {
                                "amount": 100,
                                "price": 0.002
                            },
                            "storage": {
                                "amount": 580,
                                "price": 0.00005
                            }
                        },
                        "status": {
                            "listed": true,
                            "online": true,
                            "report": "https://monitor.m.tensordock.com/report/uptime/12c94b1b3c8471877d59005b08eb693e/",
                            "uptime": 0.9999
                        }
                    }
                },
                "success": true
            }
        """
        return self._make_request(f'deploy/hostnodes?minGPUCount={min_gpu_count}', method='get')

    def get_hostnode_details(self, hostnode_uuid):
        """
        Retrieve details for a specific hostnode.

        Args:
            hostnode_uuid (str): UUID of the hostnode.

        Returns:
            dict: A dictionary containing details of the specified hostnode.

        Example response:
            {
                "success": true,
                "02c65d45-6da5-4232-a8db-ee0e5bc76110": {
                    "location": {
                        "city": "Winnipeg",
                        "country": "Canada",
                        "dc": null,
                        "id": "50cf200c-be1b-4983-a316-369d2eea10ec",
                        "region": "Manitoba"
                    },
                    "networking": {
                        "ports": [20013, 20012, 20011, 20010, 20009],
                        "receive": 1000,
                        "send": 1000
                    },
                    "specs": {
                        "cpu": {
                            "amount": 26,
                            "price": 0.003,
                            "type": "AMD Ryzen 9 5950X"
                        },
                        "gpu": {
                            "geforcertx3080-pcie-10gb": {
                                "amount": 1,
                                "price": 0.15
                            }
                        },
                        "ram": {
                            "amount": 100,
                            "price": 0.002
                        },
                        "storage": {
                            "amount": 580,
                            "price": 0.00005
                        }
                    },
                    "status": {
                        "listed": true,
                        "online": true,
                        "report": "https://monitor.m.tensordock.com/report/uptime/12c94b1b3c8471877d59005b08eb693e/",
                        "uptime": 0.9999
                    }
                }
            }
        """
        return self._make_request(f'deploy/hostnodes/{hostnode_uuid}', method='get')

    def deploy_vm(self, **kwargs):
        """
        Deploy a new virtual machine.

        Args:
            **kwargs: Keyword arguments for VM deployment, including:
                password (str): Password for the VM.
                ssh_key (str, optional): SSH key for the VM.
                name (str): Name of the VM.
                gpu_count (int): Number of GPUs.
                gpu_model (str): GPU model.
                vcpus (int): Number of vCPUs.
                ram (int): Amount of RAM in GB.
                external_ports (list): List of external ports.
                internal_ports (list): List of internal ports.
                hostnode (str): UUID of the hostnode.
                storage (int): Storage amount in GB.
                operating_system (str): Operating system for the VM.

        Returns:
            dict: A dictionary containing deployment information.

        Example response:
            {
                "cost": {
                    "compute_price": 0.238,
                    "storage_price": 0.005,
                    "total_price": 0.243
                },
                "execution_id": 1689,
                "ip": "mass-a.tensordockmarketplace.com",
                "port_forwards": {
                    "30117": "80",
                    "30118": "22"
                },
                "server": "65e7edca-888a-4e66-a975-2c6cd4cd218b",
                "success": true
            }
        """
        return self._make_request('deploy/single', kwargs)

    def validate_spot_price_new(self, **kwargs):
        """
        Validate spot instance price for a new VM.

        Args:
            **kwargs: Keyword arguments for spot price validation, including:
                gpu_count (int): Number of GPUs.
                gpu_model (str): GPU model.
                vcpus (int): Number of vCPUs.
                hostnode (str): UUID of the hostnode.
                ram (int): Amount of RAM in GB.
                storage (int): Storage amount in GB.
                price (float): Bid price for the spot instance.

        Returns:
            dict: A dictionary containing the validation result.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('spot/validate/new', kwargs)

    def validate_spot_price_existing(self, server, price):
        """
        Validate spot instance price for an existing VM.

        Args:
            server (str): UUID of the existing VM.
            price (float): New bid price for the spot instance.

        Returns:
            dict: A dictionary containing the validation result.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('spot/validate/existing', {'server': server, 'price': price})

    def list_vms(self):
        """
        List all virtual machines for the organization.

        Returns:
            dict: A dictionary containing information about all VMs.

        Example response:
            {
                "success": true,
                "virtualmachines": {
                    "65e7edca-888a-4e66-a975-2c6cd4cd218b": {
                        "cost": 0.238,
                        "location": "edffaa9d-c4d3-46eb-bdf6-fad125dbeae7",
                        "hostnode": "84352cea-7bc8-4859-8a5c-d173a98ca236",
                        "name": "My RTX 4000 Server",
                        "operating_system": "Ubuntu 20.04 LTS",
                        "port_forwards": {
                            "30117": "80",
                            "30118": "22"
                        },
                        "specs": {
                            "gpu": {
                                "amount": 1,
                                "type": "rtxa4000-pcie-16gb"
                            },
                            "ram": 32,
                            "vcpus": 8
                        },
                        "status": "Running",
                        "timestamp_creation": "Sat, 10 Dec 2022 21:38:19 GMT"
                    }
                }
            }
        """
        return self._make_request('list')

    def get_vm_details(self, server):
        """
        Get details of a specific virtual machine.

        Args:
            server (str): UUID of the VM.

        Returns:
            dict: A dictionary containing details of the specified VM.

        Example response:
            {
                "success": true,
                "virtualmachine": {
                    "cost": 0.1,
                    "hostname": "217.79.242.232",
                    "hostnode": "8db2ec46-c094-4262-bc7e-6c76617f4237",
                    "location": "d52421f8-b264-440f-b9fb-78e05f2af72f",
                    "name": "test",
                    "operating_system": "Ubuntu 22.04 LTS",
                    "port_forwards": {
                        "60098": "22"
                    },
                    "specs": {
                        "gpu": {
                            "amount": 8,
                            "type": "v100-pcie-16gb"
                        },
                        "ram": 8,
                        "storage": 100,
                        "vcpus": 16
                    },
                    "status": "Outbid",
                    "timestamp_creation": "Sun, 21 May 2023 16:18:35 GMT",
                    "type": "spot"
                }
            }
        """
        return self._make_request('get/single', {'server': server})

    def start_vm(self, server):
        """
        Start a virtual machine.

        Args:
            server (str): UUID of the VM to start.

        Returns:
            dict: A dictionary containing the start operation result.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('start/single', {'server': server})

    def stop_vm(self, server, disassociate_resources=False):
        """
        Stop a virtual machine.

        Args:
            server (str): UUID of the VM to stop.
            disassociate_resources (bool, optional): Whether to release the GPU when stopping. Defaults to False.

        Returns:
            dict: A dictionary containing the stop operation result.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('stop/single', {'server': server, 'disassociate_resources': disassociate_resources})

    def modify_vm(self, server_id, **kwargs):
        """
        Modify a virtual machine's specifications.

        Args:
            server_id (str): UUID of the VM to modify.
            **kwargs: Keyword arguments for VM modification, which may include:
                gpu_model (str): New GPU model.
                gpu_count (int): New number of GPUs.
                ram (int): New amount of RAM in GB.
                vcpus (int): New number of vCPUs.
                storage (int): New storage amount in GB.

        Returns:
            dict: A dictionary containing the modification result.

        Example response:
            {
                "server": "cb3c501e-b85c-473d-9ab1-04dbb3e28450",
                "success": true
            }
        """
        kwargs['server_id'] = server_id
        return self._make_request('modify/single', kwargs)

    def delete_vm(self, server):
        """
        Delete a virtual machine.

        Args:
            server (str): UUID of the VM to delete.

        Returns:
            dict: A dictionary containing the deletion result.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('delete/single', {'server': server})
