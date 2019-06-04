"""
Problem
Consider the leftmost and righmost appearances of some value in an array.
We'll say that the "span" is the number of elements between the two inclusive.
A single value has a span of 1. Returns the largest span found in the given
array. (Efficiency is not a priority.)

maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
"""

from collections import defaultdict

def maxSpan(l):
    """
    l = list

    Returns max span of a given list

    The algorithm preprocess the list in order to optimize the efficiency.

    Preprocess the list l to store a dictionary of each unique value with its
    indices. This helps to optimize the computation of number of elements
    between the same value. Suppose element 1 occurs at index 1 and index 4.
    v is the dictionary of list of indices. v[1] = [1, 4]
    Then max_span = v[1][-1] - v[1][0] + 1 = 4, where -1 refers to last index

    Cons: Space Complexity O(n)
    Pros: Improvement in time complexity to O(n) from O(n^2)
    """
    if l is None or len(l) == 0:
        # Empty list: max span = 0
        max_span = 0
        print("maxSpan({}) = {}, empty list".format(l, max_span))
        print("\tOccurs from a empty element")
        print()
        return max_span

    # Preprocess a list into dictionary of value -> list of indices where
    # value occurs
    indices = defaultdict(list)
    for i, x in enumerate(l):
        indices[x].append(i)

    # To store each unique value's max span
    # The data type for each element of the list is a tuple in order to print
    # meaningful message at the end.
    # The tuple is (k, span_value, i, j) where
    # k is the unique value in the list
    # i is the index value where first k occurs in a list,
    # j is the index value where last k occurs after index i
    all_spans = list()

    k_m, max_span, i, j = 0, 0, -1, -1

   # Retrieve the maximum span of all the unique values in the list
   # And compute the max span of each unique value in the list
    for k, v in indices.items():

        # There is one unique element in list: max span = 1
        # v[-1] - v[0] + 1 = 1.
        # Or
        # At least two elements in list: max span = number of elements
        # between them inclusively.
        # The maximum span range from the first occurance of k to
        # the last occurance of k in the indices
        m = v[-1] - v[0] + 1

        # storing each unique span value to print later
        all_spans.append((k, m, v[0], v[-1]))

        if m > max_span:
            k_m, max_span, i, j = k, m, v[0], v[-1]

    # Prints maxSpan of list
    if max_span == 1:
        print("maxSpan({}) = {}, for single element {}".format(l, max_span, k))
    else:
        # max_span > 1
        print("maxSpan({}) = {}".format(l, max_span))

    # Prints where the max spans occurs
    for k_, m_, i_, j_ in all_spans:
        if max_span == m_:
            if max_span > 1:
                print("\tOccurs from {} at index {} to {} at index {}"
                      .format(k_, i_, k_, j_))
            else:
                print("\tOccurs from a single element {} at index {}"
                      .format(k_, i_))

    # Prints each unique element's max span
    print("\tMax spans (k, max, i, j) for each unique value k are = {}"
          .format(all_spans))
    print()
    return max_span

if  __name__ == "__main__":
    maxSpan(None)
    maxSpan([])
    maxSpan([1, 2, 3, 4, 5])
    maxSpan([1, 2, 1, 1, 3])
    maxSpan([1, 4, 2, 1, 4, 1, 4])
    maxSpan([1, 4, 2, 1, 4, 4, 4])
