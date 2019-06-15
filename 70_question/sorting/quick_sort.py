# Best: O(n log n) time | O(log n) space
# Best: O(n log n) time | O(log n) space
# Worst: O(n^2) time | O(log n) space
def quick_sort(array):
    quick_sort_pivot_first(array, 0, len(array) - 1)
    return array

def quick_sort_pivot_first(a, start, end):
    """
    a : array
    start: inclusive index
    end: inclusive index
    a[start:end+1] = array to sort
    Using the first elemennt as pivot.
    """
    # Base case
    if len(a) <=1 or start > end:
        return

    # Select first/start element as the pivot
    pivot, n = start, len(a)

    # Assign the left and right pointer
    left, right = start + 1, end

    while left <= right:
        # 3. swap since left pointer value should be lesser than a[pivot]
        if a[left] > a[right]:
            swap(a, left, right)

        # 1. keep going until a[left] > a[pivot]
        if a[left] <= a[pivot]:
            left += 1

        # 2. keep going until a[right] < a[pivot]
        if a[right] >= a[pivot]:
            right -= 1

    # 4. adjust the pivot
    swap(a, right, pivot)

    # 5. value in the pivot is sorted in place.
    # And, quick sort the remaining two halves.
    # quick sort the smaller half first, then the bigger half.
    if end - right + 1 < right - 1 - start + 1:
        quick_sort_pivot_first(a, right+1, end)
        quick_sort_pivot_first(a, start, right-1)
    else:
        quick_sort_pivot_first(a, start, right-1)
        quick_sort_pivot_first(a, right+1, end)

def swap(a, x, y):
    a[x], a[y] = a[y], a[x]

