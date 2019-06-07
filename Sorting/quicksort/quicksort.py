"""
QUICKSORT(A, left, right):
    if left < right:
        index = PARTITION(A, left, right)
        QUICKSORT(A,left, index-1)
        QUICKSORT(A, index, right)

To sort an entire array A, the initial call is QUICKSORT(A, 0, len(A)-1)

Partition the array

The key to the algorithm is the PARTITION procedure, which rearranges the
subarray A[left ... right ] in place.
"""

def quicksort(arr, left, right, debug=False):
    """
    arr = list of numbers to sort
    left = low index
    right = high index
    returns a sorted ascending list of number

    partition uses  midpoint as pivot to partition the array
    """
    if left >= right:
        # Base case where left reference and right reference has cross the
        # pivot
        return

    if debug: print("before index: left={} right={}".format(left, right))

    # Conquer the problem by sorting in this partition
    index = partition(arr, left, right)

    if debug:
        print("after index left={} right={} index={}"
              .format(left, right, index))
        print()

    # Divide the problem into smaller arrays
    quicksort(arr, left, index - 1)
    quicksort(arr, index, right)

def swap(arr, left, right):
    """
    helper method to swap arr[left] and arr[right] values in place.
    """
    arr[left], arr[right] = arr[right], arr[left]

def partition(arr, left, right, debug=False):
    """
    Returns the partition index where the array is to be divide/split

    """

    pivot = (left+right)//2

    if debug:
        print("before parition: arr={} pivot={} at index={}, left={}, right={}"
              .format(arr, arr[pivot], pivot, left, right))

    while left <= right:
        # traverse until the left index where arr[left] >= arr[pivot]
        while arr[left] < arr[pivot]:
            left += 1

        # traverse until the right index where arr[right] <= arr[pivot]
        while arr[right] > arr[pivot]:
            right -= 1

        # If left is within left half and right is within right half
        # then Values needs to swap because the values are incorrect
        # Otherwise, the iteration ends.
        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1

    if debug:
        print("after parition: arr={} pivot={} at index={}, left={}, right={}"
              .format(arr, arr[pivot], pivot, left, right))
    return left


if __name__ == "__main__":

    arr = [15, 3, 9, 8, 5, 2, 7, 1, 6]
    print("Before array is sorted:", arr)
    quicksort(arr, 0, len(arr)-1)
    print("After array is sorted:", arr)
