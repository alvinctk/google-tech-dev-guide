from typing import List
class Solution:
    def xpeakIndexInMountainArray(self, A: List[int]) -> int:
        """
        Time complexity = O(n)
        """
        n = len(A)
        i = 0
        while i + 1 < n and A[i] < A[i + 1]:
            i += 1
        return i

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        """
        Time complexity = O(log n)
        Your runtime beats 98.91 % of python3 submissions.
        """
        n = len(A)
        left, right = 1, n - 2
        while left <= right:
            mid = left + (right - left)//2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                left = mid + 1
            elif A[mid - 1] > A[mid]:
                right = mid - 1
