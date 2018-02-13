"""Authentication Interface"""
from abc import ABCMeta, abstractmethod


class Authentication:
    """Confirm the legitimacy of a user"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_legit(self, entity_id):
        """Verify entity's legitimacy

        param: entity_id: the id of the enetity
        return: an integer indicating active, disabled, inactive, etc.
        """

    @abstractmethod
    def is_admin(self, entity_id):
        """Verify admin's legitimacy

        param: entity_id: the id of the enetity
        return: success or failure
        """
