# Unofficial TensorDock Python SDK

This is an unofficial Python SDK for interacting with the TensorDock Marketplace API. It provides a convenient way to manage virtual machines, containers, and billing information programmatically. Please note that this SDK is not officially supported or endorsed by TensorDock.

## Installation

You can install this unofficial TensorDock Python SDK using pip:

```
pip install unofficial-tensordock-python-sdk
```

## Configuration

To use the SDK, you'll need to obtain an API key and token from the TensorDock marketplace. You can get these from your TensorDock dashboard at https://marketplace.tensordock.com/api

## Usage

Here's a quick example of how to use the SDK:

```python
from unofficial_tensordock import TensorDockAPI

# Initialize the API client
api = TensorDockAPI(api_key='your_api_key', api_token='your_api_token')

# List your virtual machines
vms = api.virtual_machines.list_vms()
print(vms)

# Deploy a new virtual machine
new_vm = api.virtual_machines.deploy_vm(
    name="My New VM",
    gpu_count=1,
    gpu_model="rtx3080-pcie-10gb",
    vcpus=4,
    ram=16,
    storage=100,
    operating_system="Ubuntu 20.04 LTS"
)
print(new_vm)
```

## Features

This unofficial SDK aims to provide access to the following TensorDock API endpoints:

- Authorization
- Servers
- Virtual Machines
- Containers
- Billing

For a full list of features and their implementations, please refer to the source code or the inline documentation.

## Documentation

For detailed documentation on each method, please refer to the inline docstrings in the source code. For official API documentation, please visit the [TensorDock API Documentation](https://marketplace.tensordock.com/api).

## Contributing

Contributions to this unofficial TensorDock Python SDK are welcome! Please feel free to submit issues, fork the repository and send pull requests. As this is an unofficial project, community involvement is crucial for its maintenance and improvement.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues related to this unofficial SDK, please open an issue on our [GitHub repository](https://github.com/yourusername/unofficial-tensordock-python-sdk).

For questions about the TensorDock API itself or for official support, please contact TensorDock directly through their official channels.

## Acknowledgements

This project is based on the public API documentation provided by TensorDock. We are grateful for their detailed documentation which makes this unofficial SDK possible.
