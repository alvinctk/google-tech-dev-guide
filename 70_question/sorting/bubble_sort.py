# Best case: O(n) time | O(1) space   => since array is already sorted
# Average case:  O(n^2) time | O(1) space
# Worst case: O(n^2) time | O(1)
def bubblesort(array):
    if not array:
        return array
    i, swap, n = 0, 0, len(array)

    while i < n - 1:
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            swap += 1
        if n - 2 == i:
            if not swap:
                break
            else:
                i = 0
                swap = 0
        else:
            i += 1
    return array

if __name__ == "__main__":
    array = [2, 1, 8, 33, 4, -1, 5, 7]
    bubblesort(array)
    print(array)
