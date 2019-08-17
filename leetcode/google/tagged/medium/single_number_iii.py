from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Time complexity: O(N) linear scan
        Space complexity: O(1)
        """
        # Find the bit that contains two numbers
        x = 0
        for i in nums:
            x ^= i

        # Find the first rightmost bit that two numbers that differs
        # A 1 bit can be resulted by 1 or 0 from either one number.
        # 1 = 1 ^ 0.
        mask = -x & x

        x1 = 0
        x2 = 0
        for i in nums:
            # The two different numbers differs by the mask bit
            if i & mask:
                x1 ^= i
            else:
                x2 ^= i

        return [x1, x2]

if __name__ == "__main__":

    x = [1,2,1,3,2,5]
    y = [2, 2, 4, 4, 5, 3]
    z = [-112, -112, -6, -6, -5, 3]
    a = [1, 2, 1, 3, 2, 5]
    s = Solution()
    for nums in [x, y, z, a]:
        print(s.singleNumber(nums))

