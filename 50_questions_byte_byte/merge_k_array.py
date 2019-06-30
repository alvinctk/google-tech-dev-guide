"""
Given k sorted array, merge them into a single sorted array
"""



def merge_k_array(k_array):
    array = []
    length = [len(i_array) for i_array in k_array]
    i = 0
    while any(filter(lambda x: x > 0, length)):
        for k in range(len(length)):
            if length[k]:
                array.append(k_array[k][i])
                length[k] -= 1
        i += 1

    heapsort(array)
    print("The {} has sorted and merged into {}".format(k_array, array))

def heapsort(array):
    n = len(array)
    for i in range(n-1):

       # Build max heap from 0 to n-1-i
       max_heapify(array, n - 1 - i)

       # Swap the biggest value to the back.
       swap(array, 0, n - 1 - i, n)

def max_heapify(array, end):
    n = len(array)

    parent = (end - 1)//2
    while parent >= 0:

        left = 2 * parent + 1
        right = 2 * parent + 2

        if left <= end and array[left] > array[parent]:
            swap(array, left, parent, n)

        if right <= end and array[right] > array[parent]:
            swap(array, right, parent, n)

        parent -= 1

def swap(array, a, b, n):
    if a < n and b < n:
        array[a], array[b] = array[b], array[a]

if __name__ == "__main__":
    merge_k_array([[1, 2, 3], [5, 6, 7], [10, 11, 12]])
    merge_k_array([[1, 2, 3], [5, 6], [10, 11, 12, 13]])
