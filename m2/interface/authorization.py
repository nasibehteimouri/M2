"""Auhtorization Interface"""
from abc import ABCMeta, abstractmethod


class Authorization:
    """Specify access rights/privileges to resources"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def check_entity_node_access(self, entity_id, node_mac_addres):
        """Authorize entity's access to reserve a specific node

        param: entity_id: the id of the enetity
        param: node_mac_addres: the mac address of the node
        return: success or failure
        """

    def check_entity_instance_access(self, entity_id, instance_id):
        """Authorize entity's access to a provisioned instance

        param: entity_id: the id of the enetity
        param: instance_id: the id of the provisioned instance
        return: success or failure
        """

    def check_entity_storage_access(self, entity_id, storage_id):
        """Authorize entity's access to read/write from/to a storage

        param: entity_id: the id of the enetity
        param: storage_id: the id of the storage
        return: success or failure
        """

    def check_entity_image_access(self, entity_id, instance_id):
        """Authorize entity's access to an image

        param: entity_id: the id of the enetity
        param: image_id: the id of the image
        return: success or failure
        """

    def check_entity_tag_access(self, entity_id, tag_id):
        """Authorize entity's access to a tag

        param: entity_id: the id of the enetity
        param: tag_id: the id of the tag
        return: success or failure
        """

    def check_entity_network_access(self, entity_id, network_id):
        """Authorize entity's access to a network

        param: entity_id: the id of the enetity
        param: network_id: the id of the tag
        return: success or failure
        """
