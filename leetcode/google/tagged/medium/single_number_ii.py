from typing import List
from collections import Counter
class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        """
        Every element appears three items except for one, which appear exactly once.
        Returns the single element.

        N = number of elements
        Time complexity: O(N) to iterate over the input array
        Space complexity: O(N) to keep the set of N/3 elements
        Runtime: 68 ms, faster than 72.91% of Python3 online submissions for Single Number II.
        Memory Usage: 15.8 MB, less than 6.67% of Python3 online submissions for Single Number II.
        """

        return (3*sum(set(nums)) - sum(nums))//2

    def singleNumber2(self, nums: List[int]) -> int:
        """
        Every element appears three items except for one, which appear exactly once.
        Returns the single element.

        N = number of elements
        Time complexity: O(N) to iterate over the input array
        Space complexity: O(N) to keep the count of N/3 elements

        Runtime: 56 ms, faster than 99.64% of Python3 online submissions for Single Number II.
        Memory Usage: 15.7 MB, less than 6.67% of Python3 online submissions for Single Number II.
        """
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k

    def singleNumber2(self, nums: List[int]) -> int:
        """
        Every element appears three items except for one, which appear exactly once.
        Returns the single element.

        N = number of elements
        Time complexity: O(N) to iterate over the input array
        Space complexity: O(N) to keep the count of N/3 elements

        Runtime: 56 ms, faster than 99.64% of Python3 online submissions for Single Number II.
        Memory Usage: 15.7 MB, less than 6.67% of Python3 online submissions for Single Number II.
        """
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k


    def singleNumber(self, nums: List[int]) -> int:
        """
        Every element appears three items except for one, which appear exactly once     .
        Returns the single element.

        N = number of elements
        Time complexity: O(N) to iterate over the input array
        Space complexity: O(1)

        Runtime: 72 ms, faster than 47.40% of Python3 online submissions for Single Number II.
        Memory Usage: 15.7 MB, less than 6.67% of Python3 online submissions for Single Number II.
        """
        # k = 3 (binary 11), m = 2, 2**m = 4 > k => need a mask => mask = ~(x1 & x2)
        # p = 2 (binary 10), x2 = 1, x1 = 0, so return x2. Or alternatively, return x1 | x2
        # k = 3

        x1 = x2 = 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x2 | x1






