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

def max_span(l):
    """
    l = list

    Returns max span of a given list

    The algorithm preprocess the list in order to optimize the efficiency.

    Preprocess the list l to store a dictionary of each unique value with its
    indices. This helps to optimize the computation of number of elements
    between the same value. Suppose element 1 occurs at index 1 and index 4.
    v is the dictionary of list of indices. v[1] = [1, 4]
    Then max_span = v[1][i+1] - v[i][i] + 1 = 4, where i+1 = 4 and i=1

    Cons: Space Complexity O(n)
    Pros: Improvement in time complexity to O(n)
    """

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
    # i is the index value where k occurs in a list,
    # j is the index value where k occurs after index i
    all_spans = list()

    # Compute the max span of each unique value in the list
    for k, v in indices.items():

        if v is None:
            # Empty list: max span = 0
            all_spans.append((k, 0, -1, -1))

        elif len(v) == 1:
            # Only one unique element in list: max span = 1
            all_spans.append((k, 1, v[0], -1))

        else:
            # At least two elements in list: max span = number of elements
            # between them inclusively.
            spans = [(v[i+1] - v[i] + 1, v[i], v[i+1]) for i, _ in enumerate(v[:-1])]
            max_spans = max(spans, key=lambda x: x[0])

            all_spans.append((k, max_spans[0], max_spans[1], max_spans[2]))

    # Retrieve the maximum span of all the unique values in the list
    k, m, i, j = max(all_spans, key=lambda x: x[1]) if all_spans is not None else (-1, 0, -1, -1)

    # Prints maxSpan of list
    if m == 0:
        print("maxSpan({}) = {}, empty list)".format(l, m))
    elif m == 1:
        print("maxSpan({}) = {}, for single element {}".format(l, m, k))
    else:
        print("maxSpan({}) = {}".format(l, m))

    # Prints where the max spans occurs
    for k_, m_, i_, j_ in all_spans:
        if m == m_:
            if m > 1:
                print("\tOccurs from {} at index {} to {} at index {}".format(k_, i_, k_, j_))
            elif m == 1:
                print("\tOccurs from a single element {} at index {}".format(k_, i_))
            elif m == 0:
                print("\tOccurs from a empty element")

    # Prints each unique element's max span
    print("\tMax spans (k, max, i, j) for each unique value k are = {}".format(all_spans))
    print()

    return m

if  __name__ == "__main__":

    max_span([1, 2, 3, 4, 5])
    max_span([1, 2, 1, 1, 3])
    max_span([1, 4, 2, 1, 4, 1, 4])
    max_span([1, 4, 2, 1, 4, 4, 4])


