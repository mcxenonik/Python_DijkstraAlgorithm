class Node:
    def __init__(self, new_id=None, new_value=None):
        self.id = new_id
        self.value = new_value

    def get_id(self):
        return self.id

    def get_value(self):
        return self.value

    def __str__(self):
        return f'NODE: ID={self.id} | VALUE={self.value}'