from collections import deque

class Heap:
    def __init__(self, greater=None):
        self.array = deque()
        self.greater = greater

    def diff(self, other):
        return abs(len(self) - len(other))

    def __len__(self):
        return len(self.array)

    def insert(self, x):
        self.array.append(x)
        self.heapify()

    def peek(self):
        return self.array[0] if self.array else None

    def remove_top(self):
        remove = self.array.popleft()
        self.heapify()
        return remove

    def parent(self, i):
        return (i - 1)//2

    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def heapify(self):
        n = len(self.array)
        parent = self.parent(n - 1)

        while parent >= 0:
            left = 2 * parent + 1
            right = 2 * parent + 2
            if right < n:
                if self.greater and self.array[right] > self.array[parent]:
                    self.swap(right, parent)
                elif not self.greater and self.array[right] < self.array[parent]:
                    self.swap(right, parent)

            if left < n:
                if self.greater and self.array[left] > self.array[parent]:
                    self.swap(left, parent)
                elif not self.greater and self.array[left] < self.array[parent]:
                    self.swap(left, parent)

            parent -= 1

class Median_Heap:
    def __init__(self):
        self.min_heap = Heap(greater=False)
        self.max_heap = Heap(greater=True)
        self.median = 0

    def diff(self):
        return abs(len(self.min_heap) - len(self.max_heap))

    def balance(self):
        if self.diff() <= 1:
            return
        print("balance", self.max_heap.array, self.min_heap.array)
        min_heap_more = True if len(self.min_heap) > len(self.max_heap) else False
        while self.diff() > 1:
            if min_heap_more and self.min_heap.array:
                self.max_heap.insert(self.min_heap.remove_top())
            elif not min_heap_more and self.max_heap.array:
                self.min_heap.insert(self.max_heap.remove_top())

    def insert(self, x):
        if len(self.max_heap) == 0:
            self.max_heap.insert(x)
        elif x > self.max_heap.peek():
            self.min_heap.insert(x)
        else:
            self.max_heap.insert(x)
        self.balance()
        self.set_median()
        print(self.median, x, self.max_heap.array, self.min_heap.array)

    def set_median(self):
        if self.diff() == 0:
            self.median = (self.min_heap.peek() + self.max_heap.peek()) / 2
        elif len(self.min_heap) > len(self.max_heap):
            self.median = self.min_heap.peek()
        else:
            self.median = self.max_heap.peek()

    def get_median(self):
        return self.median


if __name__ == "__main__":
    mh = Median_Heap()
    for x in [5, 10, 100, 200, 6, 13, 14]:
        mh.insert(x)

