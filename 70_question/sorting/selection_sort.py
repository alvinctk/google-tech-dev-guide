# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selection_sort(a):
    """
    Use selection sort algorithm to sort array/list
    """
    i, n = 0, len(a)
    while i < n - 1:
        j, small = i + 1, i
        while j < n:
            if a[small] > a[j]:
                small = j
            j += 1
        a[i], a[small] = a[small], a[i]
        i += 1
    return a

if __name__ == "__main__":
    x = [8, 5, 2, 9, 5, 6, 3]
    print("Array before sorted: {}".format(x))
    selection_sort(x)
    print("Array after sorted: {}".format(x))

