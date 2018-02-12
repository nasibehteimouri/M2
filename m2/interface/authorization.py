from abc import ABCMeta, abstractmethod


class Authorization:
    """Class for specifying access rights/privileges to resources"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def autherize_access_node(self, node_id):
        """Autherize entity's access to a specific node"""

    @abstractmethod
    def autherize_access_image(self, image_id):
        """Autherize entity's access to a specific image"""

    @abstractmethod
    def autherize_access_tag(self, tag_id):
        """Autherize entity's access to a specific tag"""
