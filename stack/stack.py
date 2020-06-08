"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.append = self.add_to_tail
        self.pop = self.remove_tail

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        count = 0
        for n in self:
            count += 1
        return count

    def add_to_head(self, item):
        n = Node(item)
        n.next = self.head
        self.head = n
        if self.head.next is None:
            self.tail = n

    def add_to_tail(self, item):
        n = Node(item)
        if self.head is None:
            self.head = n
            self.tail = n
            n.next = None
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = n
        n.next = None
        self.tail = n

    def remove_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.value
        current_node = self.head
        previous_node = None
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        removed = self.tail
        self.tail = previous_node
        return removed.value

    def remove_head(self):
        if self.head is None:
            return None
        removed = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return removed.value

    def get_max(self):
        if self.head is None:
            return None
        max_num = 0
        for n in self:
            if n.value > max_num:
                max_num = n.value
        return max_num

    def contains(self, item):
        for n in self:
            if n.value == item:
                return True
        return False


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

    def __repr__(self):
        return self.value



class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.storage = LinkedList()
   
    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        try:
            return self.storage.pop()
        except IndexError:
            return None





