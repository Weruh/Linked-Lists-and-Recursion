
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.

    Recursion is used for sum, reverse, and search because a linked list is
    itself a recursive structure: a list is either empty (None) or a node
    followed by a smaller list. Each method handles one node and delegates the
    rest of the list to a recursive call, which keeps the logic short and clear.

    Note: Python's default recursion limit (~1000 frames) means these methods
    are intended for small-to-moderate lists, which suits this demonstration.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """Insert a new node at the head of the list. O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Append a new node to the tail of the list. O(n) to reach the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """Return the sum of all node data, computed recursively. O(n)."""

        def _sum(node):
            # Base case: an empty list (or the end of the list) contributes 0.
            if node is None:
                return 0
            # Recursive case: this node's value plus the sum of the rest.
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        """Reverse the list in-place by re-pointing each node's `next`. O(n)."""

        def _reverse(prev, current):
            # Base case: we've walked past the last node, so `prev` is the
            # old tail, which becomes the new head.
            if current is None:
                return prev
            # Recursive case: save the rest of the list, point this node
            # back at the previous one, then reverse the remainder.
            next_node = current.next
            current.next = prev
            return _reverse(current, next_node)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """Return True if `target` is in the list, otherwise False. O(n)."""

        def _search(node):
            # Base case 1: reached the end without a match.
            if node is None:
                return False
            # Base case 2: found it, so stop recursing.
            if node.data == target:
                return True
            # Recursive case: look in the rest of the list.
            return _search(node.next)

        return _search(self.head)

    def to_list(self):
        """Return the node values as a Python list, head first."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values

    def __str__(self):
        return " -> ".join(str(value) for value in self.to_list() + ["None"])

    def display(self):
        """Print the list as 'val -> val -> val -> None'."""
        print(self)
