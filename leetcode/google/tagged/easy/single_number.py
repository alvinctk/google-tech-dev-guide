from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(n) since algorithm scan all n elements
        Space complexity: O(1) constant space

        Runtime: 96 ms, faster than 86.96% of Python3 online submissions for Single Number.
        Memory Usage: 16.3 MB, less than 6.56% of Python3 online submissions for Single Number.
        """
        # k = 2(binary 11), p = 1 (binary 01), m = 1, 2^m = 2 == k => no need mask
        x1 = 0
        for i in nums:
            x1 ^= i
        return x1
