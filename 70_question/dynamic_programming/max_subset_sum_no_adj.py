def maxSubsetSumNoAdjacent(array, debug=True):
    """
    For a given array length of n, the maximum subset sum of non adjacent
    elements last position can occurs at either at n-1 or n-2.

    We know that max sum for last position n-1 can compute by
       max_sum[n-1] = max_sum[(n-1)-2] + array[(n-1)]
    And, for last position n-2, the max sum is given as
       max_sum[n-2] =  max_sum[(n-1)-1]

    To generalize the formula, set n-1 to i,
       max_sum[i] = { max(
                        max_sum[i-2] + array[i]
                        max_sum[i-1]
                      )                        for all i >= 2,
                      max(array[0], array[1])  for i = 1,
                      array[i]                 for i = 0
                      where i=0 is start of array and i=n-1 is the last
                    }
    """
    if not array:
        return 0
    n = len(array)

    # The initial max_sum[i-2] occurs at i = 0
    last_two_sum = array[0]
    if n == 1:
        return last_two_sum

    # The initial max_sum[i-1] occurs at i = 1
    last_one_sum = max(array[0], array[1])
    if n == 2:
        return last_one_sum

    i, max_sum = 2, -float('inf')

    while i < n:
        # Max sum forumla for i >= 2
        max_sum = max(last_one_sum, last_two_sum + array[i])

        # Moving forward, now max_sum becomes last_one sum for next iteration
        last_two_sum, last_one_sum = last_one_sum, max_sum
        i += 1

    if debug:
        print("The max subset sum of non-adjacent in {} = {}"
              .format(array, max_sum))

    return max_sum


if __name__ == "__main__":

    array = [10, 5, 20, 25, 15, 5, 5, 15]
    maxSubsetSumNoAdjacent(array)
