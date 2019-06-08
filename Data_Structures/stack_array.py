"""
List(or array) implementation of a stack
Space used must be linear in the number of items in a stack


Stack() -> creates a new Stack object
.is_empty()
len() -> number of elements in stack
.push(item) -> push item into Stack
.pop() -> Remove and return the most recent item in the stack
"""
class Stack:
    """
    List(or array) implementation of a stack
    """
    def __init__(self):
        """
        Initialize the stack
        """
        self.top = []

    def __len__(self):
        """
        Returns the len of a stack
        For example:
        s = Stack()
        len(s)  gives 0
        """
        return len(self.top)

    def __str__(self):
        """
        Returns the string representation of a stack
        """
        this_str = "Stack: Top of stack ["
        n = len(self.top)
        for i, current in enumerate(self.top):
            this_str += str(current)
            if i + 1 < n:
                this_str += " -> "
        this_str += "] Bottom of stack; length = {}".format(len(self.top))
        return this_str

    def is_empty(self):
        """
        Returns True if the stack has no items and empty; Otherwise, False
        """
        return len(self.top) == 0

    def push(self, item):
        """
        Add item into the stack following first in last out (LIFO)
        That is, the most recently added element is at the top of the stack.
        Returns None
        """
        # Reassign the link to top of the stack and update the
        self.top = [item] + self.top

    def pop(self):
        """
        Remove the top item in the stack
        Returns the top item of the stack
        """
        popped_node = self.top[0]
        self.top = self.top[1:]
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
