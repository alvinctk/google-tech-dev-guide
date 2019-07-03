"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0
"""
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(array, n, rowIndex):
            if n > rowIndex:
                return array
            if n == 0:
                array = [1]
            elif n == 1:
                array = [1, 1]
            else:
                m = len(array) - 1

                # Generate the pascal row in-place by calculating from right to
                # left.
                left, right = m - 1, m
                array.append(array[-1])
                while left >= 0:
                    array[right] = array[right] + array[left]
                    left -= 1
                    right -= 1

            return helper(array, n+1, rowIndex)

        return helper([], 0, rowIndex)
if __name__ == "__main__":
    x = Solution()
    print(x.getRow(3))
    print(x.getRow(4))
