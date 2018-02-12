"""Interface for Target"""
from abc import ABCMeta, abstractmethod


class Authorization:
    """Class for specifying target"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def target(self, conf_file):
        """Creates a target"""

    @abstractmethod
    def add_target(self, clone_ceph_name):
        """Add a new target with given image"""

    @abstractmethod
    def remove_target(self, clone_ceph_name):
        """Remove a target"""

    @abstractmethod
    def delete_target(self, clone_ceph_name):
        """delete a target"""

    @abstractmethod
    def list_targets(self):
        """Show list of targets"""
