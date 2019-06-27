# Best O(N) | Avg O(N) | Worse O(N^2) time
# O(1) space since sort in place.
def quickselect(array, k):
    """
    Select the kth smallest element in the array
    Using quick select algorithm
    """

    n = len(array)
    if n == 1:
        print_result(array, k)
        return array[k-1]

    start, end = 0, n - 1

    while start <= end:

        # Select the first/start element as pivot
        # Assign left and right pointer
        pivot, left, right = start, start + 1, end

        while left <= right:

            # 3. Swap since left pointer value must be less than right.
            if array[left] > array[right]:
                swap(array, left, right)

            # 1. Keep going until array[left] > array[pivot]
            if array[left] <= array[pivot]:
                left += 1

            # 2. keep going until array[right] < array[pivot]
            if array[right] >= array[pivot]:
                right -= 1

        # 4. Adjust the pivot since elements to the right of array[right] are all greater than pivot.
        swap(array, right, pivot)

        if right + 1 == k:
            print_result(array, k)
            return array[right]

        # 5. Select the half that k belongs to.
        if k - 1 < right:
            end = right - 1
        else:
            start = right + 1

    print_result(array, k)
    return array[k-1]

def swap(array, left, right):
    array[left], array[right] = array[right], array[left]

def print_result(array, k):
    print("The {}th smallest element in {} is {}".format(k, array, array[k-1]))


if __name__ == "__main__":
    quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5)
