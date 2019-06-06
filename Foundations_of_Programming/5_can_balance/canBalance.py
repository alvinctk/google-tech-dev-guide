"""
Problem:

Given a non-empty array, return true if there is a place to split the array so
that the sum of the numbers on one side is equal to the
sum of the numbers on the other side.

canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true
"""

def canBalance(arr):
    """
    Determine if a list of numbers is balance.

    Parameter:
        arr := list of numbers

    Return:
        True if a split position can be found in the arr such that
        both halves sum of numbers are equal.
        False otherwise.

    Assuming numbers can be integers or float
    """
    show_result = lambda b: print("canBalance({}) = {}".format(arr, b))

    # Empty list or None cannot be split
    if arr is None or len(arr) == 0:
        show_result(False)
        return False

    total = sum(arr)
    half = 0

    # Compute if there is a balance half of sum equal to other half.
    for x in arr:
        if half == total/2:
            break
        half += x
    else:
        # Loop complete successfully without break
        # Therefore, there isn't any split in the array such that the sum of
        # the numbers on one side is equal to the sum of numbers on the other
        # side.
        show_result(False)
        return False

    show_result(True)
    return True

def canBalance2(arr):
    """
    Determine if a list of numbers is balance.

    Parameter:
        arr := list of numbers

    Return:
        True if a split position can be found in the arr such that
        both halves sum of numbers are equal.
        False otherwise.

    Assuming numbers can be only integers
    """
    show_result = lambda b: print("canBalance2({}) = {}".format(arr, b))

    # Empty list or None cannot be split
    if arr is None or len(arr) == 0:
        show_result(False)
        return False

    total = sum(arr)

    # Since numbers are only integers, there will be no balance for
    # odd numbers.
    if total % 2 != 0:
        show_result(False)
        return False

    half = 0

    # Compute if there is a balance half of sum equal to other half.
    for x in arr:
        if half == total/2:
            break
        half += x
    else:
        # Loop complete successfully without break
        # Therefore, there isn't any split in the array such that the sum of
        # the numbers on one side is equal to the sum of numbers on the other
        # side.
        show_result(False)
        return False

    show_result(True)
    return True

if __name__ == "__main__":
    canBalance([1, 1, 1, 2, 1])
    canBalance([2, 1, 1, 2, 1])
    canBalance([10, 10])

    print()

    canBalance2([1, 1, 1, 2, 1])
    canBalance2([2, 1, 1, 2, 1])
    canBalance2([10, 10])
