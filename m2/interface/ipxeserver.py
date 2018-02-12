"""Interface for ipxe srver"""
from abc import ABCMeta, abstractmethod


class Ipxeserver:
    """Class for specifying ipxe"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def ipxeserver(self):
        """setup ipxe"""

    @abstractmethod
    def generate_ipxe_file(self, node_name, target_name):
        """Generate ipxe file"""
