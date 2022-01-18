class Edge:
    def __init__(self, new_id=None, new_start_node=None, new_end_node=None, new_cost=None):
        self.id = new_id
        self.start_node = new_start_node
        self.end_node = new_end_node
        self.cost = new_cost

    def get_id(self):
        return self.id

    def get_start_node(self):
        return self.start_node

    def get_end_node(self):
        return self.end_node

    def get_cost(self):
        return self.cost

    def __str__(self):
        start_node = str(self.start_node)
        end_node = str(self.end_node)

        return f'EDGE: ID={self.id} | START_NODE=({start_node}) | END_NODE=({end_node}) | COST={self.cost}'