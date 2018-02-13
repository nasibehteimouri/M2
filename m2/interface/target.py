"""Target Interface"""
from abc import ABCMeta, abstractmethod


class Authorization:
    """Specify provisioning target"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_target(self, clone_name):
        """Registers a new target with given image
	param: clone_name: 
        return: 
        """

    @abstractmethod
    def remove_target(self, clone_ceph_name):
        """Remove a target
        
        """

    @abstractmethod
    def list_targets(self):
        """Show list of targets

        """

    @abstractmethod
    def get_target_id(self):
        """Show list of targets

        """
