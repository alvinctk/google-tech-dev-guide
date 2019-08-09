from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        """
        Runtime: 236 ms, faster than 79.18% of Python3 online submissions for Valid Mountain Array.
        Memory Usage: 15.2 MB, less than 5.26% of Python3 online submissions for Valid Mountain Array.
        """
        n = len(A)
        if n < 3 or A[0] >= A[1] or A[n-2] <= A[n-1]:
            return False

        i = 1
        while i < n:
            if A[i - 1] < A[i]:
                i += 1
            else:
                break

        if i == n or A[i-1] == A[i]:
            return False

        while i < n:
            if A[i - 1] > A[i]:
                i += 1
            else:
                return False

        return i == n


    def validMountainArray2(self, A: List[int]) -> bool:
        """
        does not work
        """
        n = len(A)
        if n < 3 or A[0] >= A[1] or A[n-2] <= A[n-1]:
            return False

        left, right = 1, n-2

        while left <= right:
            increasing = A[left - 1] < A[left]
            decreasing = A[right] > A[right + 1]
            print(increasing, "left", left, A[left - 1], A[left])
            print(decreasing, "right", right, A[right], A[right + 1])
            if not increasing and not decreasing:
                return False
            elif left == right:
                return True

            if increasing and left + 1 <= right and A[left] < A[left+1]:
                left += 1

            if decreasing and left <= right - 1  and A[right - 1] > A[right]:
                right -= 1

        return right == left

if __name__ == "__main__":
    s = Solution()
    s.validMountainArray([1, 2, 3, 5, 4, 3, 2, 1])
    print()
    s.validMountainArray([0, 3, 2, 1])
    print()
    s.validMountainArray([3, 5, 5])
    print()
