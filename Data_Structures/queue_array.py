"""
List(or array) implementation of a First In First Out (FIFO) Queue
Space used must be linear in the number of items in a queue

Queue() -> creates a new Queue object
.is_empty()
len() -> number of elements in queue
.enqueue(item) -> enqueue item into queue
.dequeue() -> Remove and return the most recent item in the queue
"""
class Queue:
    """
    List(or array) implementation of a queue
    """
    def __init__(self):
        """
        Initialize the queue
        """
        self.queue = []

    def __len__(self):
        """
        Returns the len of a queue
        For example:
        q = Queue()
        len(q)  gives 0
        """
        return len(self.queue)

    def __str__(self):
        """
        Returns the string representation of a Queue
        """
        this_str = "Queue: Front of queue ["
        n = len(self.queue)
        for i, current in enumerate(self.queue):
            this_str += str(current)
            if i + 1 < n:
                this_str += " -> "
        this_str += "] End of queue; length = {}".format(len(self.queue))
        return this_str

    def is_empty(self):
        """
        Returns True if the queue has no items and empty; Otherwise, False
        """
        return len(self.queue) == 0

    def enqueue(self, item):
        """
        Add item into the queue following first in first out (FIFO)
        That is, the most recently added element is at the end of the queue.
        Returns None
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Returns and remove the first item that joins the queue
        """
        dequeue_node = self.queue[0]
        self.queue = self.queue[1:]
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
