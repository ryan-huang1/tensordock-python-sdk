from .api import TensorDockAPI

# tensordock/api.py
from .endpoints.authorization import Authorization
from .endpoints.servers import Servers
from .endpoints.virtual_machines import VirtualMachines
from .endpoints.containers import Containers
from .endpoints.billing import Billing

class TensorDockAPI:
    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token
        self.base_url = "https://marketplace.tensordock.com/api/v0"

        self.authorization = Authorization(self)
        self.servers = Servers(self)
        self.virtual_machines = VirtualMachines(self)
        self.containers = Containers(self)
        self.billing = Billing(self)
