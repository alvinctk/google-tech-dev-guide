# O(log n) time | O(1) space
def shiftedBinarySearch(array, target, debug=False, result=True):
    left, right = 0, len(array) - 1
    while left < right:

        # Select random pivot
        mid = left + (right-left)//2

        # Ensure the left side of the pivot is a monotonic increasing sequence
        if debug: print("before shifted pivot", mid)
        while left <= mid - 1 and array[left] > array[mid]:
            mid -= 1
        if debug: print("after shifted pivot", mid)


        if target == array[left]:
            # Optimize to prevent further calls to get left = mid
            if result: print_result(array, target, left)
            return left

        elif target == array[right]:
            # Optimize to prevent further calls to get right = mid
            if result: print_result(array, target, right)
            return right

        elif target == array[mid]:
            if result: print_result(array, target, mid)
            return mid

        elif array[left] <= target and target <= array[mid]:
            # Select the left half
            right = mid - 1
            if debug: print("left", array[left:right+1], mid, array[mid], array)
        else:
            # Select the right half
            left = mid + 1
            if debug: print("right", array[left:], mid, array[mid], array)

    if result: print_result(array, target, -1)
    return -1

def print_result(array, target, index):
    print("Index position of target {} in array {} = {}".format(target, array, index))
if __name__ == "__main__":
    x = [71, 72, 73, 0, 1, 21, 23, 33, 45, 45, 61]
    array = [33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21]
    target = 355
    shiftedBinarySearch(x, 73)
    shiftedBinarySearch(array, target)
