def twoNumberSum_0(array, targetSum):
    """
    Space complexity: O(1)
    Time complexity: O(n^2)
    """
    for i, first_value in enumerate(array):
        j = i + 1
        while j < len(array):
            second_value = array[j]
            if targetSum == first_value + second_value:
                if first_value < second_value:
                    return [first_value, second_value]
                else:
                    return [second_value, first_value]
            j += 1
    return []

def twoNumberSum_1(array, targetSum):
    """
    Space complexity: O(n) => using dictionary as hash table
    Time complexity: O(n) => only process the array list once
    """
    d = dict()
    for i, value in enumerate(array):
        remainder = targetSum - value
        if remainder in d:
            if value < remainder:
                return [value, remainder]
            else:
                return [remainder, value]
        else:
            d[value] = i
    # Not found
    return []

def twoNumberSum_2(array, targetSum):
    """
    Space complexity: O(1) => using array in place
    Time complexity: O(n log n) => due to array.sort
    """
    # Sort array in-place
    array.sort()
    left, right = 0, len(array)-1

    while left < right:
        l, r = array[left], array[right]
        current_sum = l + r

        if current_sum == targetSum:
            return [l, r]
        elif current_sum > targetSum:
            # array[right] value is too large.
            # We have to select the next largest value in the sorted array
            right -= 1
        else:
            # array[left] value is too small
            # We have to select the next smallest value in the sorted array
            left += 1
    return []

