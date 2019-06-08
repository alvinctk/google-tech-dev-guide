"""
Linked list implementation of a stack
Space used must be linear in the number of items in a stack


Stack() -> creates a new Stack object
.is_empty()
len() -> number of elements in stack
.push(item) -> push item into Stack
.pop() -> Remove and return the most recent item in the stack
"""
class Node:
    """
    Node class to represent each single node
    Mainly used as a linked list
    """
    def __init__(self, item, next_item):
        self.item = item
        self.next_item = next_item

    def __str__(self):
        return str(self.item)

class Stack:
    """
    Linked list implementation of a stack
    """

    def __init__(self):
        """
        Initialize the stack
        """
        self.top = None
        self.length = 0

    def __len__(self):
        """
        Returns the len of a stack
        For example:
        s = Stack()
        len(s)  gives 0
        """
        return self.length

    def __str__(self):
        """
        Returns the string representation of a stack
        """
        current = self.top
        this_str = "Stack: Top of stack ["
        while current is not None:
            this_str += str(current)
            if current.next_item is not None:
                this_str += " -> "
            current = current.next_item
        this_str += "] Bottom of stack; length = {}".format(self.length)
        return this_str

    def is_empty(self):
        """
        Returns True if the stack has no items and empty; Otherwise, False
        """
        return self.length == 0

    def push(self, item):
        """
        Add item into the stack following first in last out (LIFO)
        That is, the most recently added element is at the top of the stack.
        Returns None
        """
        # Reassign the link to top of the stack and update the
        self.top = Node(item, self.top)
        self.length += 1

    def pop(self):
        """
        Remove the top item in the stack
        Returns the top item of the stack
        """
        if self.top is None:
            return None
        else:
            popped_node = self.top

            # Reassign the top node
            self.top = self.top.next_item

            # Remove popped node next link
            popped_node.next_item = None

            # Update length
            self.length -= 1

            return popped_node

if __name__ == "__main__":
    s = Stack()
    # Test stack
    for x in [1, 2, 3, 4 ,5]:
        s.push(x)
        print(s)

    x = Stack()
    while not s.is_empty():
        x.push(s.pop())
        #print("x", x)
        #print("s", s)
    s.push(None)
    print("x", x)
    print("s", s)
