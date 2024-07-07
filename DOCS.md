# Unofficial TensorDock Python SDK - Detailed Documentation

This document provides a comprehensive overview of all methods available in the Unofficial TensorDock Python SDK. The SDK is organized into several modules, each corresponding to a different aspect of the TensorDock API.

## Table of Contents

1. [Initialization](#initialization)
2. [Authorization](#authorization)
3. [Virtual Machines](#virtual-machines)
4. [Containers](#containers)
5. [Billing](#billing)

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

**Returns:** A dictionary containing the success status.

**Example response:**

```python
{
    "success": true
}
```

### List Authorizations

Get a list of all authorizations for your account.

```python
authorizations = api.authorization.list_authorizations()
```

**Returns:** A dictionary containing the success status and a list of authorizations.

**Example response:**

```python
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
```

## Virtual Machines

### Get Available Hostnodes

Retrieve a list of all available hostnodes.

```python
hostnodes = api.virtual_machines.get_available_hostnodes(min_gpu_count=0)
```

**Parameters:**

- `min_gpu_count` (int, optional): Minimum number of GPUs required. Defaults to 0.

**Returns:** A dictionary containing information about available hostnodes.

**Example response:**

```python
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
```

### Get Hostnode Details

Get detailed information about a specific hostnode.

```python
details = api.virtual_machines.get_hostnode_details(hostnode_uuid='hostnode_uuid')
```

**Parameters:**

- `hostnode_uuid` (str): The UUID of the hostnode.

**Returns:** A dictionary containing detailed information about the specified hostnode.

**Example response:**

```python
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
```

### Deploy VM

Deploy a new virtual machine.

```python
new_vm = api.virtual_machines.deploy_vm(**kwargs)
```

**Parameters:**

- `**kwargs`: Keyword arguments for VM deployment, including:
  - `password` (str): Password for the VM.
  - `ssh_key` (str, optional): SSH key for the VM.
  - `name` (str): Name of the VM.
  - `gpu_count` (int): Number of GPUs.
  - `gpu_model` (str): GPU model.
  - `vcpus` (int): Number of vCPUs.
  - `ram` (int): Amount of RAM in GB.
  - `external_ports` (list): List of external ports.
  - `internal_ports` (list): List of internal ports.
  - `hostnode` (str): UUID of the hostnode.
  - `storage` (int): Storage amount in GB.
  - `operating_system` (str): Operating system for the VM.

**Returns:** A dictionary containing deployment information.

**Example response:**

```python
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
```

### Validate Spot Price (New VM)

Validate spot instance price for a new VM.

```python
result = api.virtual_machines.validate_spot_price_new(**kwargs)
```

**Parameters:**

- `**kwargs`: Keyword arguments for spot price validation, including:
  - `gpu_count` (int): Number of GPUs.
  - `gpu_model` (str): GPU model.
  - `vcpus` (int): Number of vCPUs.
  - `hostnode` (str): UUID of the hostnode.
  - `ram` (int): Amount of RAM in GB.
  - `storage` (int): Storage amount in GB.
  - `price` (float): Bid price for the spot instance.

**Returns:** A dictionary containing the validation result.

**Example response:**

```python
{
    "success": true
}
```

### Validate Spot Price (Existing VM)

Validate spot instance price for an existing VM.

```python
result = api.virtual_machines.validate_spot_price_existing(server='vm_uuid', price=0.5)
```

**Parameters:**

- `server` (str): UUID of the existing VM.
- `price` (float): New bid price for the spot instance.

**Returns:** A dictionary containing the validation result.

**Example response:**

```python
{
    "success": true
}
```

### List VMs

Get a list of all your virtual machines.

```python
vms = api.virtual_machines.list_vms()
```

**Returns:** A dictionary containing information about all your VMs.

**Example response:**

```python
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
```

### Get VM Details

Get detailed information about a specific VM.

```python
details = api.virtual_machines.get_vm_details(server='vm_uuid')
```

**Parameters:**

- `server` (str): The UUID of the VM.

**Returns:** A dictionary containing detailed information about the specified VM.

**Example response:**

```python
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
```

### Start VM

Start a stopped VM.

```python
result = api.virtual_machines.start_vm(server='vm_uuid')
```

**Parameters:**

- `server` (str): The UUID of the VM to start.

**Returns:** A dictionary containing the start operation result.

**Example response:**

```python
{
    "success": true
}
```

### Stop VM

Stop a running VM.

```python
result = api.virtual_machines.stop_vm(server='vm_uuid', disassociate_resources=False)
```

**Parameters:**

- `server` (str): The UUID of the VM to stop.
- `disassociate_resources` (bool, optional): Whether to release the GPU when stopping the VM. Defaults to False.

**Returns:** A dictionary containing the stop operation result.

**Example response:**

```python
{
    "success": true
}
```

### Modify VM

Modify the specifications of a VM.

```python
result = api.virtual_machines.modify_vm(server_id='vm_uuid', **kwargs)
```

**Parameters:**

- `server_id` (str): The UUID of the VM to modify.
- `**kwargs`: Keyword arguments for VM modification, which may include:
  - `gpu_model` (str): New GPU model.
  - `gpu_count` (int): New number of GPUs.
  - `ram` (int): New amount of RAM in GB.
  - `vcpus` (int): New number of vCPUs.
  - `storage` (int): New amount of storage in GB.

**Returns:** A dictionary containing the modification result.

**Example response:**

```python
{
    "server": "cb3c501e-b85c-473d-9ab1-04dbb3e28450",
    "success": true
}
```

### Delete VM

Delete a VM.

```python
result = api.virtual_machines.delete_vm(server='vm_uuid')
```

**Parameters:**

- `server` (str): The UUID of the VM to delete.

**Returns:** A dictionary containing the deletion result.

**Example response:**

```python
{
    "success": true
}
```

## Containers

### Deploy Container

Deploy a new container.

```python
new_container = api.containers.deploy_container(**kwargs)
```

**Parameters:**

- `**kwargs`: Keyword arguments for container deployment, including:
  - `display_name` (str): The name of your container.
  - `project_id` (str): The ID that will be used to identify the container on each VM.
  - `image_name` (str): The name of the image to deploy on Docker Hub.
  - `registry_type` (str): Either "public" or "private" registry.
  - `gpu_count` (int): Number of GPUs to deploy per container replica.
  - `gpu_models` (list): List of GPU models to deploy on.
  - `replicas` (int): Number of container replicas to deploy.
  - `ram` (int): Amount of RAM per container replica.
  - `vcpus` (int): Number of vCPUs per container replica.
  - `storage` (int): Storage per container replica.
  - `networking_port` (int): Port exposed by your Docker image.
  - `environment_variables` (dict): Environment variables for the container.
  - `volumes` (list): List of volumes to mount.
  - `arguments` (list): List of arguments for the container.
  - `max_vm_rate_hourly` (float): Maximum hourly rate of each container replica.

**Returns:** A dictionary containing the deployment status.

**Example response:**

```python
{
    "success": true
}
```

### Scale Container

Scale a container by adding or removing replicas.

```python
result = api.containers.scale_container(container_id='container_uuid', replicas=3)
```

**Parameters:**

- `container_id` (str): ID of the container to scale.
- `replicas` (int): Number of replicas to add (positive) or remove (negative).

**Returns:** A dictionary containing the scaling status.

**Example response:**

```python
{
    "success": true
}
```

### Stop Container

Stop a container.

```python
result = api.containers.stop_container(container_id='container_uuid')
```

**Parameters:**

- `container_id` (str): ID of the container to stop.

**Returns:** A dictionary containing the stop status.

**Example response:**

```python
{
    "success": true
}
```

### Get Container Replicas

Get information about a container's replicas.

```python
replicas = api.containers.get_container_replicas(container_id='container_uuid')
```

**Parameters:**

- `container_id` (str): ID of the container to get replicas for.

**Returns:** A dictionary containing information about the container's replicas.

**Example response:**

```python
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
```

## Billing

### Get Balance

Get the current balance and spending rate for your account.

```python
balance_info = api.billing.get_balance()
```

**Returns:** A dictionary containing the current balance and hourly cost.

**Example response:**

```python
{
    "balance": 999.987,
    "hourly_cost": 0.856,
    "success": true
}
```

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

**Returns:** A dictionary containing revenue data for each hostnode.

**Example response:**

```python
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
```

### Get Monthly Summary

For hosting providers, get a monthly summary of earnings.

```python
summary = api.billing.get_monthly_summary(period='2023-05')
```

**Parameters:**

- `period` (str): The month to get the summary for, in YYYY-MM format.

**Returns:** A dictionary containing the monthly summary of earnings and transactions.

**Example response:**

```python
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
```
