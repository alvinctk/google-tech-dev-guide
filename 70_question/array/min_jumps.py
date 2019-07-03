# O(nk) time and O(n) space
# O(n) time for one pass iterating through the array
# O(k) time for min function where k is the number of items to be min
def minNumberOfJumps(array, debug=False):

    n = len(array)
    min_jumps = [0] * n
    i = n-2
    while i >= 0:
        if array[i] != 0:
            furthest_can_jump = min(i + array[i], n - 1)
            previous_min_jump = min(min_jumps[i+1:furthest_can_jump+1])
            min_jumps[i] = 1 + previous_min_jump
        else:
            min_jumps[i] = float("inf")

        if debug:
            print("    array", array)
            print("min_jumps", min_jumps)
            print()
        i -= 1
    minimum_jumps = min_jumps[0] if min_jumps[0] != float("inf") else -1
    print("miniumn jumps to reach end is {}".format(minimum_jumps))

    return minimum_jumps

# 70 questions solution but doesn't work when jump value is zer
def min_j(array, debug=False):
    jumps = 0
    max_reach = array[0]
    steps = array[0]
    for i in range(1, len(array)-1):
        if debug:
            print("i", i, "max_reach", max_reach, "steps", steps, "jumps", jumps)
            print("max_reach, i+array[i], steps", max_reach, i + array[i], steps)
        max_reach = max(max_reach, i + array[i])
        steps -= 1
        if debug:

            print("max_reach, steps", max_reach, steps)

        if steps == 0:
            if debug: print("before add jumps steps", jumps, steps)
            jumps += 1
            steps = max_reach - i
            if debug: print("after add jumps steps", jumps, steps)

        if debug:
            print("    array", array)
            print()
    print("min jumps is ", jumps+1)
    return jumps+1

if __name__ == "__main__":

    minNumberOfJumps([2, 3, 1, 1, 4])
    minNumberOfJumps([3, 2, 1, 0, 4])
    minNumberOfJumps([3, 0, 1, 2, 4])

    min_j([2, 3, 1, 1, 4])
    min_j([3, 0, 1, 2, 4])
    min_j([3, 2, 1, 0, 4])
