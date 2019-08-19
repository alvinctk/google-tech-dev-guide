from typing import List
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 32 ms, faster than 88.02% of Python3 online submissions for First Bad Version.
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 36 ms, faster than 65.18% of Python3 online submissions for First Bad Version.
        Time complexity O(log n)
        Space complexity O(log n) recursive depth
        """
        def helper(left, right):
            mid = left + (right - left)//2

            good, bad = not isBadVersion(mid - 1), isBadVersion(mid)
            if bad and (mid == 1 or good):
                return mid

            if bad:
                return helper(left, mid - 1)
            else:
                return helper(mid + 1, right)

        return helper(1, n)
