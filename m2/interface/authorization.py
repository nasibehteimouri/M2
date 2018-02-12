from abc import ABCMeta, abstractmethod


class Authorization:
    """Class for specifying access rights/privileges to resources"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def authorize_access_node(self, node_id):
        """Authorize entity's access to a specific node"""

    @abstractmethod
    def authorize_access_image(self, image_id):
        """Authorize entity's access to a specific image"""

    @abstractmethod
    def authorize_access_tag(self, tag_id):
        """Authorize entity's access to a specific tag"""
