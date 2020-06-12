"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        l_height = -1
        r_height = -1
        if self.node:
            if self.node.left:
                self.node.left.update_height()
                l_height = self.node.left.height
            if self.node.right:
                self.node.right.update_height()
                r_height = self.node.right.height
            self.height = max(l_height, r_height) + 1
        else:
            self.height = -1

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        l_height = -1
        r_height = -1
        if self.node:
            if self.node.left:
                self.node.left.update_balance()
                l_height = self.node.left.height
            if self.node.right:
                self.node.right.update_balance()
                r_height = self.node.right.height
            self.balance = l_height - r_height
        else:
            self.balance = 0

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        old_root = self.node
        old_right = self.node.right.node
        old_right_left = old_right.left.node
        self.node = old_right
        old_right.left.node = old_root
        old_root.right.node = old_right_left
        self.update_height()
        self.update_balance()

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        old_root = self.node
        old_left = self.node.left.node
        old_left_right = old_left.right.node
        self.node = old_left
        old_left.right.node = old_root
        old_root.left.node = old_left_right
        self.update_height()
        self.update_balance()

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height()
        self.update_balance()
        if self.balance > 1:
            if self.node.left.balance < 0:
                self.node.left.left_rotate()
            self.right_rotate()
        if self.balance < -1:
            if self.node.right.balance > 0:
                self.node.right.right_rotate()
            self.left_rotate()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if self.node is None:
            n = Node(key)
            n.left = AVLTree()
            n.right = AVLTree()
            self.node = n
        elif key < self.node.key:
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)
        self.rebalance()

        
a = AVLTree()
a.insert(10)
a.insert(5)
