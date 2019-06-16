"""
Given an array of integers. Returns an array of length 2 representing the
largest range of numbers contained in the array.

The first number in the output array should be the first number in the range.
The second number in the output array should be the second number in the range.

A range of numbers is defined as a set of numbers that comes right after each
other in the set of real numbers. For example the output range array [2, 6]
represents the arrange [2, 3, 4, 5, 6] which is a range of length 5.

Note that numbers do not need to be ordered or adjacent in the array in order
to form a range. Assume that there will be one largest range.
"""
def largestRange(array):
    range_x, range_y = array[0], array[0]
    for x in array:
        min_v = i = x
        while i in array:
            min_v = i
            i = i - 1

        max_v = i = x
        while i in array:
            max_v = i
            i = i + 1
            if max_v - min_v + 1 > range_y - range_x + 1:
                range_y = max_v
                range_x = min_v
    return [range_x, range_y]
