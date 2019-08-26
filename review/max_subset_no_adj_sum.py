def maxSubsetSumNoAdjacent(array):
    """
    max subset non-adjacent sum = max(max_sum[i-2] + x[i], max_sum[i-1])
    """
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]

    max_sum = float()
    second = array[0]
    first = max(array[0], array[1])
    for x in array[2:]:

        current = max(second + x, first)
        second = first
        first = current

    return first
