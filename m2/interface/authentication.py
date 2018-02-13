""" Authentication Interface """
from abc import ABCMeta, abstractmethod


class Authentication:
    """ Confirm the legitimacy of a user """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_entity_id(self, user_name, user_password):
        """
        Authenticate entity's legitimacy

        param: user_name: the name of the user
        param: user_password: the password of the user

        return: entity_id: the entity to which the user belongs
        in case of success, or otherwise raise an exception
        """

    @abstractmethod
    def get_status(self, entity_id):
        """
        Return the status of an already authenticated entity

        param: entity_id: the id of the enetity
        return: an integer indicating one of the following statuses:
        0 means active,
	1 means inactive (happend after the first warning due to e.g. unpaid-bill),
        2 means revoked (happend after the end of the first warning duration),
        3 means disabled
        """

    @abstractmethod
    def ensure_admin(self, entity_id):
        """
        Authenticate admin's legitimacy, more privilege is accessible
        to admin as compared to non-admin users

        param: entity_id: the id of the enetity
        return: None in case of success, or otherwise raise an exception
        """
