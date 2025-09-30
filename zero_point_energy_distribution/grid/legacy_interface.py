# Legacy Interface for Zero Point Energy Distribution Grid

class LegacyGridInterface:
    """
    A legacy interface for managing the zero point energy distribution grid.
    """

    def __init__(self):
        self.grid_data = {}

    def add_node(self, node_id, properties):
        """
        Adds a node to the grid.
        :param node_id: Unique identifier for the node.
        :param properties: Properties associated with the node.
        """
        self.grid_data[node_id] = properties

    def remove_node(self, node_id):
        """
        Removes a node from the grid.
        :param node_id: Unique identifier for the node to be removed.
        """
        if node_id in self.grid_data:
            del self.grid_data[node_id]

    def get_node(self, node_id):
        """
        Retrieves the properties of a node.
        :param node_id: Unique identifier for the node.
        :return: Properties of the node if found, None otherwise.
        """
        return self.grid_data.get(node_id, None)

    def update_node(self, node_id, properties):
        """
        Updates the properties of an existing node.
        :param node_id: Unique identifier for the node.
        :param properties: New properties for the node.
        """
        if node_id in self.grid_data:
            self.grid_data[node_id] = properties

    def list_nodes(self):
        """
        Lists all nodes in the grid.
        :return: A dictionary of all nodes and their properties.
        """
        return self.grid_data
