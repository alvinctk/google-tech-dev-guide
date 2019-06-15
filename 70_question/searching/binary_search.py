# O(log n) time | O(1) space
def binary_search(array, target):
    n = len(array)
    left, right = 0, n - 1
    while left <= right:

        if array[left] == target:
            return left
        elif array[right] == target:
            return right

        mid = left + (right - left)//2

        if array[mid] == target:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == "__main__":
    x = [0, 1, 21, 33, 45, 45, 61, 71, 71, 73]
    print(binary_search(x, 33))
