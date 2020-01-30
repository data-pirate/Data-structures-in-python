class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_value):
        if value < current_value.value:
            if current_value.left is None:
                current_value.left = Node(value)
            else:
                self._insert(value, current_value.left)
        elif value > current_value.value:
            if current_value.right is None:
                current_value.right = Node(value)
            else:
                self._insert(value, current_value.right)
        else:
            print('\'{}\' already exists in the tree !'.format(value))

    def print_tree(self):
        if not self.root is None:
            self._print_tree(self.root)
        else:
            print('alert ! Empty tree, add some values to the tree')

    def _print_tree(self,value):
        # in-order traversals
        if not value is None:
            self._print_tree(value.left)
            print(value.value)
            self._print_tree(value.right)

a = BST()
a.insert(101)
a.insert(121)
a.insert(111)
a.insert(187)
a.insert(11)
a.insert(167)
a.insert(45)

a.print_tree()