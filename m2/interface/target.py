""" Diskless Interface """
from abc import ABCMeta, abstractmethod


class Diskless:
    """ Specify provisioning target """
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_target(self, instance_id, image_id):
        """
        Create a provisioning target to provision an instance using an image
        param: instance_id: the id of the provisioned instance
        param: image_id: the id of the image
        return: target_id: the id of the provisioning target
        """

    @abstractmethod
    def delete_target(self, instance_id):
        """
        Remove a target
        param: instance_id: the id of the provisioned instance
        return: none in case of success, or otherwise raise an exception
        """

    @abstractmethod
    def get_target_id(self, instance_id):
        """
        Get the provisioning target id used for provisioning
        param: instance_id: the id of the provisioned instance
        return: target_id: the id of the provisioning target
        """
