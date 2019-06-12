class Node:
    """
    Node class
    """
    def __init__(self, value):
        """
        to initalize
        """
        self.prev = None
        self.next = None
        self.value = value

    def __str__(self):
        """
        str
        """
        return "Node({})".format(self.value)

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insert(self, value):
        """
        Insert at the end/tail
        """
        self.insertAfter(self.tail, Node(value))

    def insert_front(self, value):
        """
        Insert at the head
        """
        self.insertBefore(self.head, Node(value))

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        # Update the inserted node
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # Update the previous node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        # Update the current node
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        if node is None:
            self.setHead(nodeToInsert)
            return

        # Update the inserted node
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        # Update the node after inserted node
        if nodeToInsert.next is None:
            self.tail = nodeToInsert
        else:
            nodeToInsert.next.prev = nodeToInsert

        # Update the current node
        node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        i = 1
        current = self.head
        while i < position and current is not None:
            i += 1
            current = current.next
            if i == position and current is not None:
                self.insertBefore(current, nodeToInsert)
            else:
                self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            toRemove = current
            current = current.next
            if toRemove.value == value:
                self.remove(toRemove)

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None and current.value != value:
            current = current.next
        return current is not None and current.value == value

    def print_ll(self, head=True):
        print("self.head = {}".format(str(self.head)))
        print("self.tail = {}".format(str(self.tail)))

        if self.head is None:
            print("dll is empty")
            return

        current = self.head
        if not head:
            current = self.tail
        to_print = str(current.value)

        if head:
            current = current.next
        else:
            current = current.prev

        while current is not None:
            to_print += " -> " + str(current.value)
            if head:
                current = current.next
            else:
                current = current.prev
        print(to_print)
if __name__ == "__main__":
    ll = DoublyLinkedList()
    for x in [1, 2, 3, 4]:
        ll.insert(x)
    ll.print_ll()
    ll.print_ll(head=False)
    ll.removeNodesWithValue(2)
    ll.print_ll()
    ll.print_ll(head=False)

    ll.insert_front(5)
    ll.print_ll()
    ll.print_ll(head=False)
    ll.insert(5)
    ll.print_ll()
    ll.print_ll(head=False)
    current = ll.head
    while current is not None:
        current.remove()
