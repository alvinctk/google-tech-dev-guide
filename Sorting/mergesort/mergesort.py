"""
Asymptotic Analysis
This algorithm's running time can be expressed with the following recursive
relation:
    T(1) = O(1)
    T(n) = D(n) + 2 * T(n/2) + M(n)
where D is the time needed to divide two elements
and M is the time needed to merge them together

Worse case: O(n log n)
Best case: O(n log n) typically, O(n) natural variant
Average case: O(n log n)

Top Down Approach
This divide and conquer algorithm has three steps:
    1. Divide. Split an unordered -element sequence into two unordered
       subsequences of items.
    2. Conquer. Recursively sort the two subsequences until such a time as you
       hit the base case of one item (i.e., a list containing a single element is
    sorted with respect to itself).
    3. Stitch. Merge the two sorted subsequences into a single sorted list.
"""
def mergesort(seq, ascending=True):

    if len(seq) == 1:
        # Base case, no more split, sequence only has one element
        return

    # Midpoint for division
    mid = len(seq)//2
    left, right = seq[:mid], seq[mid:]

    # Divide into halves
    mergesort(left, ascending)  # sort the first/left half
    mergesort(right, ascending) # sort the second/right half

    i, j, k = 0, 0, 0
    n, m = len(left), len(right)

    # Merge back in place to array
    while i < n and j < m:
        if (ascending and (left[i] <= right[j])) or \
                ((not ascending) and (left[i] >= right[j])):
            seq[k] = left[i]
            i += 1
        else:
            seq[k] = right[j]
            j += 1
        k +=1

    # Check if there are any elements in the left division
    while i < n:
        seq[k] = left[i]
        i += 1
        k += 1

    # Check if there are any elements in the right divison
    while j < m:
        seq[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    seq = [12, 11, 23, 6, 1, 10]
    print("Before ascending merge sort, seq = {}".format(seq))
    mergesort(seq)
    print("After ascending merge sort, seq = {}".format(seq))
    print()
    seq = [12, 11, 23, 6, 1, 10]
    print("Before descending merge sort, seq = {}".format(seq))
    mergesort(seq, ascending=False)
    print("After descending merge sort, seq = {}".format(seq))
