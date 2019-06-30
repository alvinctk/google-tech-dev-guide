# Best/Avg/Worse O(n log n) time | O(1) space
def heapSort(array):
    n = len(array)
    i = 0

    while i < n - 1:

        # max heap from index 0 to index n - 1 - i
        max_heapify(array, n - 1 - i)

        # swap the max to the back
        swap(array, 0, n - 1 - i)
        i += 1

    return array

def max_heapify(array, end):
    """
    O(log n) to build max heap
    """
    parent = (end - 1)//2

    while parent >= 0:

        child_left = 2 * parent + 1
        child_right = 2 * parent + 2

        if child_left <= end and array[child_left] > array[parent]:
            swap(array, parent, child_left)

        if child_right <= end and array[child_right] > array[parent]:
            swap(array, parent, child_right)

        parent -= 1

def max_heapify_x(array, end):
    """
    O(N) to build max heap
    """
    while end > 0:

        parent = (end-1)//2

        if array[end] > array[parent]:
            swap(array, parent, end)

        end -= 1

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
