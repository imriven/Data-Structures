class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_start(self, item):
        n = Node(item)
        n.next = self.head
        self.head = n

    def add_end(self, item):
        n = Node(item)
        if self.head is None:
            self.head = n
            n.next = None
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            continue
        current_node.next = n
        n.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll = LinkedList()
print(ll)
ll.add_start("Nina")
ll.add_start("Tiger")
ll.add_start("Leila")
ll.add_end("John")
print(ll)
