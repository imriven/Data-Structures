"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev






"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
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


    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        n = ListNode(value, None, self.head)
        if self.head is not None:
            self.head.prev = n
        else:
            self.tail = n
        self.head = n
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        removed = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return removed.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        n = ListNode(value, self.tail, None)
        if self.tail is not None:
            self.tail.next = n
        if self.head is None:
            self.head = n
        self.tail = n

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        current_tail = self.tail
        if self.tail.prev is None:
            self.head = None
        self.tail = self.tail.prev
        return current_tail.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.head == node:
            return
        if self.tail == node:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = None
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail == node:
            return
        if self.head == node:
            self.head = node.next
        else:
            node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.tail == node and self.head == node:
            self.head = None
            self.tail = None
            return
        if self.tail == node:
            self.tail = node.prev
            node.prev.next = None
            return
        if self.head == node:
            self.head = node.next
            node.next.prev = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max = 0
        for n in self:
            if n.value > max:
                max = n.value
        return max
        
