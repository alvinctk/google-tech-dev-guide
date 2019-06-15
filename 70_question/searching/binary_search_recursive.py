# O(log n) time | O(log n) space
def binary_search(array, target):
    return binary_search_value(array, target, 0, len(array)-1)

def binary_search_value(array, target, left, right):
    if left > right:
        return -1

    # Optimize to reduce further calls to get to array[mid] == target
    if target == array[left]:
        return left
    elif target == array[right]:
        return right

    mid = left + (right - left)//2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search_value(array, target, left, mid-1)
    else:
        return binary_search_value(array, target, mid+1, right)

if __name__ == "__main__":
    x = [0, 1, 21, 33, 45, 45, 61, 71, 71]
    print(binary_search(x, 33))
