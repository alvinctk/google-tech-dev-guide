"""
Solve problem - remove kth node from end of a singly linked list
"""


class Node:
    """
    Node class
    """
    def __init__(self, value, next=None):
        """
        Initialize the value of node
        """
        self.next = next
        self.value = value


class LinkedList:
    """
    Simple implementation of singly linked list that supports insert and
    display operation.
    """
    def __init__(self):
        """
        initialization
        """
        self.head = None
        self.tail = None

    def insert(self, value):
        """
        insert node to the end of the linked list
        """
        if self.head is None and self.tail is None:
            self.head = Node(value, None)
            self.tail = self.head
            return

        self.tail.next = Node(value, None)
        self.tail = self.tail.next

    def display(self):
        """
        print the order of the linked list
        """
        if self.head is None:
            print("Linked List is empty")
            return

        to_display = str(self.head.value)
        current = self.head.next
        while current is not None:
            to_display += " -> "
            to_display += str(current.value)
            current = current.next
        print(to_display)


def remove_kth_node_from_end(head: Node, k):
    """
    Assume that the linked list head has at least k nodes.
    Remove the kth node from the end of the list.
    """
    fast, slow = head, head
    i = 0
    # if i is set to 1, then set the condition in the loop to use i<=k
    while i < k:
        # To set the differences between the fast and slow pointer is kth
        # element
        fast = fast.next
        i += 1

    if fast is None:
        # Then n = k. To remove the first element from the head.
        # Or remove the nth element from end.
        # to_be_remove = head

        head.value = head.next.value
        head.next = head.next.next
        # The code below cannot be used because the global reference still
        # references to head object. Any reference changes to head is not
        # reflected to the global.
        # to_be_remove.next = None
        return

    while fast.next is not None:
        # Traverse until one element before the removal node
        fast = fast.next
        slow = slow.next

    # the slow.next is the node to be remove
    to_be_remove = slow.next
    slow.next = slow.next.next

    # Update the removal node
    to_be_remove.next = None


def test(n: int, k: int):
    """
    To test the removal of kth node from the end
    """
    ll = LinkedList()
    for i in range(n):
        ll.insert(i)
    print("Before removing {}th node from the end:".format(k), end=" ")
    ll.display()
    remove_kth_node_from_end(ll.head, k)
    print("After removing {}th node from the end:".format(k), end=" ")
    ll.display()
    print()


if __name__ == "__main__":
    test(10, 10)
    test(10, 9)
    test(10, 4)
