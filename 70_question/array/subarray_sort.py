"""
Given an array of at least length of 2. The function returns an array of index
of starting and ending indices of the smallest subarray in the input array
that needs to be sorted in place in order for the entire input array to be
sorted. If the input array is already sorted, the function should return
[-1, 1].

    Sample input = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    Sample output = [3, 9]
"""
def subarraySort(a, debug=False):
    n = len(a)
    if n <= 1:
        print(a, [-1, -1])
        return [-1, -1]
    i = 1
    not_sorted = []
    count = 0
    min_i = min_v =  float('inf')
    max_i = max_v = -float('inf')
    while i < n:
        if a[i] < a[i-1] or ((i != n-1) and a[i] > a[i+1]):

            if i < min_i:
                min_i = i
            if i > max_i:
                max_i = i

            if a[i] < min_v:
                min_v = a[i]
            if a[i] > max_v:
                max_v = a[i]
            count += 1
        i +=1
    if not count:
        print(a, [-1, -1])
        return [-1, -1]

    #min_i, max_i = not_sorted[0][0], not_sorted[-1][0]
    #min_v, max_v = not_sorted[0][1], not_sorted[0][1]
    if debug: print(min_i, max_i, min_v, max_v)
    """
    for _, x in not_sorted:
        if x < min_v:
            min_v = x
        if x > max_v:
            max_v = x
    """
    if debug: print("before finding min_i", min_i, max_i, min_v, max_v)
    i = min_i
    while i >= 1:
        if a[i-1] > min_v:
            i -= 1
        else:
            min_i = i
            break
    else:
        # For sorting ascending order, where a[i] < a[i+1] ..... < a[n]
        # Edge case: In order to include index 0 as the subarray of not sorted
        # a[0] has to satisfy a[0] >= min_i
        if debug: print("not break i ", i, a[0], min_v)
        if i == 0 and a[0] >= min_v:
            min_i = 0
    if debug: print(min_i, max_i, min_v, max_v)
    i = max_i
    while i < n-1:
        if a[i+1] < max_v:

            i += 1
        else:
            max_i = i
            break
    else:
        # For sorting ascending order, where a[i] < a[i+1] ..... < a[n]
        # Edge case: In order to include index -1 as the subarray of not sorted
        # a[-1] has to satisfy a[-1] <= max_i
        if i == n - 1 and a[-1] <= max_v:
            max_i = i

    if debug: print(min_i, max_i, min_v, max_v)
    if debug: print(not_sorted)
    print(a, [min_i, max_i])
    return [min_i, max_i]
if __name__ == "__main__":
    r = []
    e = [1]
    w = [1, 2]
    x = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    y = [1, 2, 4, 5, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    y1 = [1, 2, 4, 5, 10, 11, 7, 12, 6, 7, 10, 11, 12]
    z = [7, 8, 8, 9, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    z0 = [6, 8, 8, 9, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    z1 = [7, 8, 8, 9, 10, 11, 7, 12, 6, 7, 11, 12, 12]
    z2 = [7, 8, 8, 9, 10, 11, 7, 12, 6, 7, 11, 11, 11]
    for a in [r, e, w, x, y, z, z0, y1, z1, z2]:
        subarraySort(a)

