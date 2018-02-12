"""Interface for TFTP server"""
from abc import ABCMeta, abstractmethod


class TftpServer:
    """Class for transferring OS images"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def tftpserver(self):
        """Set up TFTP server"""

    @abstractmethod
    def generate_mac_addr_file(self, img_name, node_name, mac_addr):
        """Generate mac address file"""
