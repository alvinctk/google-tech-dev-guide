class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = Node(value, self.head)

    def remove(self):
        to_remove = self.head
        self.head = self.head.next
        to_remove.next = None

    def reverse(self):
        head = current = self.head
        prev = next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
        self.print()

    def print(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            print("->", end = " ")
            if not current.next:
                print(current.next, end ="\n")
            current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10, 1, -1):
        ll.add(i)
        ll.print()
    ll.reverse()
