"""
Water Area

You are given an array of integers. Each non-zero integer represents the
height of a pillar of width 1. Imagine water being poured over all of the
pillars and return the surface area of the water trapped between the pillars
viewed from the front. Note that spilled water should be ignored.

Sample input: [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
Sample output: 48.
"""
def waterArea(heights, debug=False):

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    i = 1
    while i < n:
        # Compute the max to the left/right of index i
        left_max[i] = max(heights[:i])
        right_max[n-1-i] = max(heights[n - i:])
        i += 1

    area = 0
    for l, r, pillar in zip(left_max, right_max, heights):
        min_height = min(l, r)
        if pillar < min_height:
            area += min_height - pillar

    if debug:
        print(heights)
        print(left_max)
        print(right_max)

    print("The water area for {} is {}".format(heights, area))
    return area

if __name__ == "__main__":
    x = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    waterArea(x)

