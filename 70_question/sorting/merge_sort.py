def mergesort(array):
    """
    Sort an array in acesending order by using merge sort algorithm
    """
    # Used only to print
    original = array.copy()

    # O(n log n) time and O(n) space
    #mergeSort_optimal(array, array.copy(), 0, len(array)-1)

    # Other solution
    # O(n log n) time and O(n log n) space
    mergeSort_helper(array)
    print("mergesort({}) = {}".format(original, array))
    # This is required for the test program. Otherwise, the array is sorted
    # in place.
    return array

# O(n log n) time and O(n) space
def mergeSort_optimal(array, aux, start, end, space=0, debug=False):
    """
    Recursive improvment solution that uses extra auxillary array space to
    avoid copying multiple times of the same array. This reduces the time
    complexity from O(n log n) to  O(n + log n) < O(n).

    In the O(n log n) space complexity - the n refers to the space as result of
    copy of an array; and, log n refers to space complexity as a result of the
    stack frame of a recursion call.

    O(n + log n)
    Since there is only one exact copy of array used in all of
    the recursion call in order to sort the array, then O(n) refers to one copy
    and the total space complexity is O(n) + O(log n) = O(n + log n).
    """
    if start == end:
        # 0. Base case: Length of parition is 1.
        return

    # 1. Using midpoint as a pivot to divide/parition the array.
    mid = start + (end - start)//2

    if debug: print("call to function: space={} array={} aux={}, start={}, end={} mid={}".format(space, array, aux, start, end, mid))

    # 2. Divide into two halves - left [start:mid+1] and right [mid:end+1]
    # mid + 1 inclusive to left half due to 0 - 1 will result in negative and
    # infinite recursion
    # aux becomes main to avoid copying aux to array if array was main.
    # Then at merge comparison portion, simply use aux to compare and copy from
    mergeSort_optimal(aux, array, start, mid, space+1)
    mergeSort_optimal(aux, array,  mid+1, end, space+1)

    if debug:
        print("Before Merge: space={} array={} aux={}, start={}, end={} mid={}".format(space, array, aux, start, end, mid))
        print(array, array[start:end+1], array[start:mid+1], array[mid+1:end+1], start, mid, end)
        print(aux, aux[start:end+1], aux[start:mid+1], aux[mid+1:end+1], start, mid, end)

    # 3. Comparsion each element and merge back to array in the right order
    i, j, k = start, mid+1, start
    while i <= mid and j <= end:
        if aux[i] < aux[j]:
            array[k] = aux[i]
            i += 1
        else:
            array[k] = aux[j]
            j += 1
        k += 1

    # 4. Remaining elements from the left partition
    while i <= mid:
        array[k] = aux[i]
        i += 1
        k += 1

    #5. Remaining elements from the right partition
    while j <= end:
        array[k] = aux[j]
        j += 1
        k += 1

    if debug:
        print(array, array[start:end+1], array[start:mid+1], array[mid+1:end+1], start, mid, end)
        print(aux, aux[start:end+1], aux[start:mid+1], aux[mid+1:end+1], start, mid, end)
        print("After Merge: space={} array={} aux={}, start={}, end={} mid={}".format(space, array, aux, start, end, mid))

# O(n log n) time and O(n log n) space
def mergeSort_helper(array):
    """
    Recursion solution that creates a copy of each parition slice for each
    recursive call.
    For space: Given O(n) is the space taken for a copy and O(log n) is the
    space taken for stack frame. The function does a local copy each stack
    frame. Therefore the function space complexity is O(n) * O(log n)
    = O(n * log n) = O(n log n)
    """

    n = len(array)
    if n <= 1:
        # 0. Base case, no more split, sequence only has one element
        return

    # 1. Using midpoint as a pivot to divide/parition an array.
    mid = n//2

    # 2. Divide into two halves - left [start:mid] and right [mid:]
    # Left/right array used are copy of array in its parition slice
    left, right = array[:mid], array[mid:]
    mergeSort_helper(left)
    mergeSort_helper(right)

    # 3. Comparsion each element and merge back to array in the right order
    n, m = len(left), len(right)
    i, j, k = 0, 0, 0
    while i < n and j < m:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # 4. Remaining elements from the left partition
    while i < n:
        array[k] = left[i]
        i += 1
        k += 1

    # 5. Remaining elements from the right partition
    while j < m:
        array[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    for array in [[3, 4, 7, 1, 5], [4, 3, 7, 1, 5]]:
        mergesort(array)
