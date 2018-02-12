"""Interface for Authentication"""
from abc import ABCMeta, abstractmethod


class Authentication:
    """Class for confirming the legitimacy of a user"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_admin(self):
        """Verify admin's authority"""

    @abstractmethod
    def is_legit(self):
        """verify user's authority"""
