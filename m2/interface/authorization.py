""" Authorization Interface """
from abc import ABCMeta, abstractmethod


class Authorization:
    """ Specify access rights/privileges to resources """
    __metaclass__ = ABCMeta

    @abstractmethod
    def check_entity_node_access(self, entity_id, node_mac_addres):
        """
        Authorize entity's access to reserve a specific node

        param: entity_id: the id of the enetity
        param: node_mac_addres: the mac address of the node
        return: None in case of success, or otherwise raise an exception
        """

    def check_entity_storage_access(self, entity_id, rbd_name):
        """
        Authorize entity's access to read/write from/to a
        specific storage.

        param: entity_id: the id of the enetity
        param: rbd_name: the name of the storage
        return: None in case of success, or otherwise raise an exception
        """

    def check_entity_network_access(self, entity_id, network_id):
        """
        Authorize entity's access to a specific NIC

        param: entity_id: the id of the enetity
        param: network_id: the NIC used in provisioning
        return: None in case of success, or otherwise raise an exception
        """
