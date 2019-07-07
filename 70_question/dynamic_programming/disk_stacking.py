
"""
disks is sorted by ascending order of height, from lowest to highest.
Let current disk be d_c such that d_c = disks[i] for 0 <= i <= len(disks)
Let other disk be d_o such that d_o = disks[j] for 0 <= j <= i

w_c, d_c, h_c = d_c
w_o, d_o, h_o = d_o

if w_o < w_c and d_o < d_c and h_o < h_c, then
    height[i] = max { height[i]
                current disk height + height[j]
"""
def diskStacking(disks):
    # Sort disks by ascending order of height
    disks.sort(key=lambda x: x[2])

    # Dynamic programming array to help compute max height
    heights = [x[2] for x in disks]

    sequences = [None for _ in disks]

    max_height_index = 0

    for i in range(1, len(disks)):
        #current_disk = disks[i]
        print("Using these disks to calculate:", disks[:i])
        print("start at i", i, "heights", heights)
        print("start at i", i, "sequences", sequences)

        for j in range(0, i):
            #other_disk = disks[j]
            print("bottom", disks[i], "top", disks[j])
            if valid_stacking(disks[j], disks[i]):
                if heights[i] <= heights[j] + disks[i][2]:
                    print("Before updated heights at ", i, j, heights)
                    print("Before updated sequences at ", i, j, sequences)
                    heights[i] = heights[j] + disks[i][2]
                    sequences[i] = j
                    print("Updated heights", heights)
                    print("Updated sequences", sequences)

        if heights[i] >= heights[max_height_index]:
            max_height_index = i
            print("max height index", max_height_index)
        print()

    result = build_sequence(disks, sequences, max_height_index)
    return result


def build_sequence(disks, sequences, max_height_index):
    sequence = []
    while max_height_index is not None:
        sequence.append(disks[max_height_index])
        max_height_index = sequences[max_height_index]
    return list(reversed(sequence))

def valid_stacking(top, bottom):
    w1, d1, h1 = top
    w2, d2, h2 = bottom
    return w1 < w2 and d1 < d2 and h1 < h2

if __name__ == "__main__":
    #diskStacking([[2, 1, 2], [3, 2, 3]])
    diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5], [1, 1, 4]])
    #diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5]])
