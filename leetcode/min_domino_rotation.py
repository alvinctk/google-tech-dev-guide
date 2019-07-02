"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""

from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            rotation_a = rotation_b = 0
            for a, b in zip(A, B):
                if x != a and x != b:
                    return -1
                elif x != a:
                    # x != a and x == b
                    rotation_a += 1
                elif x != b:
                    # x == a and x != b
                    rotation_b += 1
                # else
                #   x == a and x == b
                #   do nothing since no rotation

            # Minimum rotation to have all elements equals x in A or B
            return min(rotation_a, rotation_b)

        def print_result(rotations):
            print("min rotations for {} and {} is {}".format(A, B, rotations))

        rotations = check(A[0])
        if rotations != -1 or A[0] == B[0]:
            # Make all elements in A or B equals to A[0]
            pass
        else:
            # Make all elements in A or B equals to B[0]
            rotations = check(B[0])

        print_result(rotations)
        return rotations


if __name__ == "__main__":
    x = Solution()
    inputs = [[[2,1,2,4,2,2], [5,2,6,2,3,2]], [[3,5,1,2,3], [3,6,3,3,4]]]
    for A, B in inputs:
        x.minDominoRotations(A, B)

