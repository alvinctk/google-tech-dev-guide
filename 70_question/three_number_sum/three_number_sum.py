def threeNumberSum(array, target_sum):
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    array.sort()
    result = []
    n = len(array)
    for i, current_number in enumerate(array):
        left, right = i+1, n - 1
        while left < right:
            l, r = array[left], array[right]
            current_sum = current_number + l + r
            if current_sum > target_sum:
                # Since the current sum is too big, we have to decrease value
                right -= 1

            elif current_sum < target_sum:
                # Since the current sum is too small, we have to increase value
                left += 1
            else:
                result.append([current_number, l, r])
                # Since if increment left by one only, then sum will be too big
                # and, if decrement right by one only, then sum will be too
                # small.
                left += 1
                right -= 1
    return result

