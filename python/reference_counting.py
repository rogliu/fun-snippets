class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)  # node1: reference count = 1
node2 = Node(2)  # node2: reference count = 1

node1.next = node2  # node1: reference count = 1, node2: reference count = 2
node2.next = node1  # node1: reference count = 2, node2: reference count = 2

node2.next = None  # node1: reference count = 1, node2: reference count = 2
del node2  # node1: reference count = 1, node2: deleted


