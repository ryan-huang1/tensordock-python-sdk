import requests
from ..exceptions import TensorDockAPIException

class Containers:
    def __init__(self, api):
        self.api = api

    def _make_request(self, endpoint, data=None, method='post'):
        """
        Internal method to make API requests.
        """
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
        """
        Deploy a new container.

        Args:
            **kwargs: Keyword arguments for container deployment, including:
                display_name (str): The name of your container.
                project_id (str): The ID that will be used to identify the container on each VM.
                image_name (str): The name of the image to deploy on Docker Hub.
                registry_type (str): Either "public" or "private" registry.
                gpu_count (int): Number of GPUs to deploy per container replica.
                gpu_models (list): List of GPU models to deploy on.
                replicas (int): Number of container replicas to deploy.
                ram (int): Amount of RAM per container replica.
                vcpus (int): Number of vCPUs per container replica.
                storage (int): Storage per container replica.
                networking_port (int): Port exposed by your Docker image.
                environment_variables (dict): Environment variables for the container.
                volumes (list): List of volumes to mount.
                arguments (list): List of arguments for the container.
                max_vm_rate_hourly (float): Maximum hourly rate of each container replica.

        Returns:
            dict: A dictionary containing the deployment status.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('deploy', kwargs)

    def scale_container(self, container_id, replicas):
        """
        Scale a container by adding or removing replicas.

        Args:
            container_id (str): ID of the container to scale.
            replicas (int): Number of replicas to add (positive) or remove (negative).

        Returns:
            dict: A dictionary containing the scaling status.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('scale', {'container_id': container_id, 'replicas': replicas})

    def stop_container(self, container_id):
        """
        Stop a container.

        Args:
            container_id (str): ID of the container to stop.

        Returns:
            dict: A dictionary containing the stop status.

        Example response:
            {
                "success": true
            }
        """
        return self._make_request('stop', {'container_id': container_id})

    def get_container_replicas(self, container_id):
        """
        Retrieve information about a container's replicas.

        Args:
            container_id (str): ID of the container to get replicas for.

        Returns:
            dict: A dictionary containing information about the container's replicas.

        Example response:
            {
                "result": [
                    {
                        "external_ports": [47924, 47925, 47926],
                        "hostnode_uptime_url": "https://monitor.m.tensordock.com/report/uptime/d46eff0ca038a49d63e17e1c61161a3e",
                        "internal_ports": [22, 5000, 7000],
                        "ip_address": "149.137.246.9",
                        "rate_hourly": 0.304,
                        "vm_uuid": "ccd025cb-525d-4ac1-9691-87e01fb64e8b"
                    },
                    {
                        "external_ports": [47921, 47922, 47923],
                        "hostnode_uptime_url": "https://monitor.m.tensordock.com/report/uptime/d46eff0ca038a49d63e17e1c61161a3e",
                        "internal_ports": [22, 5000, 7000],
                        "ip_address": "149.137.246.9",
                        "rate_hourly": 0.304,
                        "vm_uuid": "cd24ed9b-5ed2-4789-9ba3-8f9a3c16d212"
                    }
                ]
            }
        """
        return self._make_request(f'{container_id}/replicas', method='get')
