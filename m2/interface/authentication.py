""" Authentication Interface """
from abc import ABCMeta, abstractmethod


class Authentication:
    """ Confirm the legitimacy of a user """
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_legit(self, user_name, user_password):
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
        return: an integer indicating active, disabled, inactive, etc.
        """

    @abstractmethod
    def is_admin(self, entity_id):
        """
        Authenticate admin's legitimacy, more privillege is accessible
        to admin as compared to non-admin users

        param: entity_id: the id of the enetity
        return: None in case of success, or otherwise raise an exception
        """
