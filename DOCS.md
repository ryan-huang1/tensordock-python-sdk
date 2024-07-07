# Unofficial TensorDock Python SDK - Detailed Documentation

This document provides a comprehensive overview of all methods available in the Unofficial TensorDock Python SDK. The SDK is organized into several modules, each corresponding to a different aspect of the TensorDock API.

## Table of Contents

1. [Initialization](#initialization)
2. [Authorization](#authorization)
3. [Servers](#servers)
4. [Virtual Machines](#virtual-machines)
5. [Containers](#containers)
6. [Billing](#billing)

## Initialization

To use the SDK, you first need to initialize the `TensorDockAPI` class with your API key and token.

```python
from unofficial_tensordock import TensorDockAPI

api = TensorDockAPI(api_key='your_api_key', api_token='your_api_token')
```

## Authorization

### Test Authorization

Test if your API key and token are valid.

```python
result = api.authorization.test_authorization()
```

**Returns:** A boolean indicating whether the authorization was successful.

### List Authorizations

Get a list of all authorizations for your account.

```python
authorizations = api.authorization.list_authorizations()
```

**Returns:** A dictionary containing information about all authorizations.

## Servers

### Get Available Hostnodes

Retrieve a list of all available hostnodes.

```python
hostnodes = api.servers.get_available_hostnodes()
```

**Returns:** A list of dictionaries, each containing details about an available hostnode.

### Get Hostnode Details

Get detailed information about a specific hostnode.

```python
details = api.servers.get_hostnode_details(hostnode_id='hostnode_uuid')
```

**Parameters:**

- `hostnode_id` (str): The UUID of the hostnode.

**Returns:** A dictionary containing detailed information about the specified hostnode.

## Virtual Machines

### Deploy VM

Deploy a new virtual machine.

```python
new_vm = api.virtual_machines.deploy_vm(
    name="My New VM",
    gpu_count=1,
    gpu_model="rtx3080-pcie-10gb",
    vcpus=4,
    ram=16,
    storage=100,
    operating_system="Ubuntu 20.04 LTS",
    password="secure_password",
    ssh_key="your_ssh_public_key",
    external_ports=[80, 22],
    internal_ports=[80, 22],
    hostnode="hostnode_uuid"
)
```

**Parameters:**

- `name` (str): Name of the VM.
- `gpu_count` (int): Number of GPUs.
- `gpu_model` (str): Model of GPU.
- `vcpus` (int): Number of virtual CPUs.
- `ram` (int): Amount of RAM in GB.
- `storage` (int): Amount of storage in GB.
- `operating_system` (str): Operating system to install.
- `password` (str, optional): Password for the VM.
- `ssh_key` (str, optional): SSH public key for authentication.
- `external_ports` (list, optional): List of external ports to open.
- `internal_ports` (list, optional): List of internal ports to map to external ports.
- `hostnode` (str, optional): UUID of the hostnode to deploy on.

**Returns:** A dictionary containing details about the newly deployed VM.

### List VMs

Get a list of all your virtual machines.

```python
vms = api.virtual_machines.list_vms()
```

**Returns:** A dictionary containing information about all your VMs.

### Get VM Details

Get detailed information about a specific VM.

```python
details = api.virtual_machines.get_vm_details(vm_id='vm_uuid')
```

**Parameters:**

- `vm_id` (str): The UUID of the VM.

**Returns:** A dictionary containing detailed information about the specified VM.

### Start VM

Start a stopped VM.

```python
result = api.virtual_machines.start_vm(vm_id='vm_uuid')
```

**Parameters:**

- `vm_id` (str): The UUID of the VM to start.

**Returns:** A boolean indicating whether the operation was successful.

### Stop VM

Stop a running VM.

```python
result = api.virtual_machines.stop_vm(vm_id='vm_uuid', disassociate_resources=False)
```

**Parameters:**

- `vm_id` (str): The UUID of the VM to stop.
- `disassociate_resources` (bool, optional): Whether to release the GPU when stopping the VM.

**Returns:** A boolean indicating whether the operation was successful.

### Modify VM

Modify the specifications of a VM.

```python
result = api.virtual_machines.modify_vm(
    vm_id='vm_uuid',
    gpu_model='new_gpu_model',
    gpu_count=2,
    ram=32,
    vcpus=8,
    storage=200
)
```

**Parameters:**

- `vm_id` (str): The UUID of the VM to modify.
- `gpu_model` (str, optional): New GPU model.
- `gpu_count` (int, optional): New number of GPUs.
- `ram` (int, optional): New amount of RAM in GB.
- `vcpus` (int, optional): New number of virtual CPUs.
- `storage` (int, optional): New amount of storage in GB.

**Returns:** A boolean indicating whether the operation was successful.

### Delete VM

Delete a VM.

```python
result = api.virtual_machines.delete_vm(vm_id='vm_uuid')
```

**Parameters:**

- `vm_id` (str): The UUID of the VM to delete.

**Returns:** A boolean indicating whether the operation was successful.

## Containers

### Deploy Container

Deploy a new container.

```python
new_container = api.containers.deploy_container(
    display_name="My Container",
    project_id="my-container-id",
    image_name="strm/helloworld-http",
    registry_type="public",
    gpu_count=2,
    gpu_models=["v100-sxm2-16gb", "l40-pcie-48gb"],
    replicas=2,
    ram=16,
    vcpus=4,
    storage=100,
    networking_port=80,
    environment_variables={},
    volumes={},
    arguments=[],
    max_vm_rate_hourly=0.9
)
```

**Parameters:**

- `display_name` (str): Name of the container.
- `project_id` (str): ID to identify the container.
- `image_name` (str): Docker image name.
- `registry_type` (str): Either "public" or "private".
- `gpu_count` (int): Number of GPUs per replica.
- `gpu_models` (list): List of GPU models in order of preference.
- `replicas` (int): Number of container replicas.
- `ram` (int): Amount of RAM per replica in GB.
- `vcpus` (int): Number of vCPUs per replica.
- `storage` (int): Storage per replica in GB.
- `networking_port` (int): Port exposed by the Docker image.
- `environment_variables` (dict, optional): Environment variables for the container.
- `volumes` (dict, optional): Volumes to mount in the container.
- `arguments` (list, optional): Additional arguments for the container.
- `max_vm_rate_hourly` (float): Maximum hourly rate for each replica.

**Returns:** A dictionary containing details about the newly deployed container.

### Scale Container

Scale the number of replicas for a container.

```python
result = api.containers.scale_container(container_id='container_uuid', replicas=3)
```

**Parameters:**

- `container_id` (str): The UUID of the container to scale.
- `replicas` (int): The new number of replicas.

**Returns:** A boolean indicating whether the operation was successful.

### Terminate Container

Terminate a container.

```python
result = api.containers.terminate_container(container_id='container_uuid')
```

**Parameters:**

- `container_id` (str): The UUID of the container to terminate.

**Returns:** A boolean indicating whether the operation was successful.

### Get Container Replicas

Get information about a container's replicas.

```python
replicas = api.containers.get_container_replicas(container_id='container_uuid')
```

**Parameters:**

- `container_id` (str): The UUID of the container.

**Returns:** A list of dictionaries, each containing information about a replica.

## Billing

### Get Balance

Get the current balance and spending rate for your account.

```python
balance_info = api.billing.get_balance()
```

**Returns:** A dictionary containing the current balance and hourly cost.

### Get Revenue

For hosting providers, retrieve revenue information.

```python
revenue_info = api.billing.get_revenue(
    start_timestamp='2023-01-01T00:00:00Z',
    end_timestamp='2023-12-31T23:59:59Z',
    hostnode_id='hostnode_uuid'
)
```

**Parameters:**

- `start_timestamp` (str, optional): Start of the period to retrieve data for.
- `end_timestamp` (str, optional): End of the period to retrieve data for.
- `hostnode_id` (str, optional): UUID of a specific hostnode to filter by.

**Returns:** A dictionary containing revenue information.

### Get Monthly Summary

For hosting providers, get a monthly summary of earnings.

```python
summary = api.billing.get_monthly_summary(period='2023-05')
```

**Parameters:**

- `period` (str): The month to get the summary for, in YYYY-MM format.

**Returns:** A dictionary containing the monthly summary of earnings and transactions.
