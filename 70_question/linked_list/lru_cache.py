"""
LRU Cache

Implement a class for a Least Recently Used (LRU) Cache.
"""
class Node:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def remove_binnings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_tail(self):
        if not self.tail:
            return

        if self.tail == self.head:
            self.head = None
            self.tail = None

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

    def set_head(self, node):
        if self.head == node:
            # node is head
            return

        elif not self.head:
            # head and tail are None
            self.head = node
            self.tail = node

        elif self.head == self.tail:
            # one element
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail

        else:
            # Either node in tail or exists within the linked list
            if self.tail == node:
                self.remove_tail()
            node.remove_binnings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def show(self):
        current = self.head
        while current:
            print(current, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print("", end="\n")

class LRUCache:
    def __init__(self, max_size):
        self.cache = {}
        self.recent = DoublyLinkedList()
        self.max_size = max_size or 1
        self.size = 0

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        else:
            self.recent.set_head(self.cache[key])
            return self.cache[key].value

    def getMostRecentKey(self):
        if self.recent and self.recent.head:
            return self.recent.head.key
        else:
            return None

    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            # reorder the DoublyLinkedList
            self.cache[key].value = value
            self.recent.set_head(self.cache[key])

        else:
            # Add to search cache dictionary
            self.cache[key] = Node(key, value, None, None)

            # Add to DoublyLinkedList head
            self.recent.set_head(self.cache[key])

            # Update size
            self.size += 1

            # Remove last element if size > m
            if self.size > self.max_size:
                key = self.recent.tail.key
                self.recent.remove_tail()
                del self.cache[key]
                self.size -= 1

if __name__ == "__main__":

    lru = LRUCache(4)
    for k, v in zip(["a", "b", "c"], [1, 2, 3]):
        lru.insertKeyValuePair(k, v)
    lru.recent.show()
    print(lru.getMostRecentKey())
    print("hi")
    print(lru.getValueFromKey("a"))
    print(lru.getMostRecentKey())
    lru.insertKeyValuePair("d", 4)

    #lru.recent.show()
    print(lru.getValueFromKey("b"))
    lru.insertKeyValuePair("a", 5)
    print(lru.getValueFromKey("a"))
