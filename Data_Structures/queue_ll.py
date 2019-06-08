"""
Linked list implementation of a queue
Space used must be linear in the number of items in a queue


Queue() -> creates a new Queue object
.is_empty()
len() -> number of elements in queue
.enqueue(item) -> push item into Queue
.dequeue() -> Remove and return the most recent item in the queue
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

class Queue:
    """
    Linked list implementation of a queue
    """
    def __init__(self):
        """
        Initialize the queue
        """
        self.front = None
        self.end =  self.front
        self.length = 0

    def __len__(self):
        """
        Returns the len of a queue
        For example:
        q = Queue()
        len(q)  gives 0
        """
        return self.length

    def __str__(self):
        """
        Returns the string representation of a queue
        """
        current = self.front
        this_str = "Queue: Front of queue ["
        while current is not None:
            this_str += str(current)
            if current.next_item is not None:
                this_str += " -> "
            current = current.next_item
        this_str += "] End of queue; length = {}".format(self.length)
        return this_str

    def is_empty(self):
        """
        Returns True if the queue has no items and empty; Otherwise, False
        """
        return self.length == 0

    def enqueue(self, item):
        """
        Add item into the queue following first in first out (FIFO)
        That is, the most recently added element is at the end of the queue.
        Returns None
        """
        if self.end is None:
            self.front = Node(item, None)
            self.end = self.front
        else:
            # Adds item to the end of the queue
            self.end.next_item = Node(item, None)

            # Updates end pointer to points to the updated end item in queue
            self.end = self.end.next_item

        # Update length
        self.length += 1

    def dequeue(self):
        """
        Remove the top item in the queue
        Returns the top item of the queue
        """
        if self.front is None:
            self.end = None
            return None
        else:
            dequeue_node = self.front

            # Reassign the front node
            self.front = self.front.next_item

            # Remove dequeue node next link
            dequeue_node.next_item = None

            # Update length
            self.length -= 1

            # Update end reference
            if self.end is dequeue_node:
                self.end = None

            return dequeue_node

if __name__ == "__main__":
    q = Queue()
    # Test queue
    for x in [1, 2, 3, 4 ,5]:
        q.enqueue(x)
        print(q)

    x = Queue()
    while not q.is_empty():
        x.enqueue(q.dequeue())
        #print("x", x)
        #print("q", q)
    q.enqueue(None)
    print("x", x)
    print("q", q)
