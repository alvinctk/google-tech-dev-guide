# O(n^2) time and O(n) space
def maxSumIncreasingSubsequence(array, debug=False):
    n = len(array)
    if n == 1:
        result = [array[0], [array[0]]]
        print_result(array, *result)
        return result

    max_sum = [num for num in array]
    seq = [None for x in array]
    max_sum[0] = array[0]
    seq[0] = None

    global_max = array[0]
    global_index = 0

    for i in range(1, n):
        max_val = float("-inf")
        max_index = None
        for j in range(0, i):
            if array[j] < array[i] and max_val < max_sum[j]:
                max_val = max_sum[j]
                max_index = j

        if debug: print("set max_sum", i, array[i], max_val, max_index)
        if array[i] + max_val > array[i]:
            max_sum[i] = array[i] + max_val
            seq[i] = max_index
        else:
            max_sum[i] = array[i]

        if global_max < max_sum[i]:
            global_max = max_sum[i]
            global_index = i

    if debug:
        print(array)
        print(max_sum)
        print(seq)
        print(global_max, global_index)

    result = []
    while global_index is not None:
        result.append(array[global_index])
        global_index = seq[global_index]

    result = result[::-1]
    print_result(array, global_max, result)
    return [global_max, result]

def print_result(array, max_sum, sub_seq):
    print("The maximum sum of increasing subsequence {} in {} is {}".format(sub_seq, array, max_sum))

if __name__ == "__main__":
    print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30, 6]))
    print(maxSumIncreasingSubsequence([5, 4, 3, 2, 1]))
    print(maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]))
    print(maxSumIncreasingSubsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))
