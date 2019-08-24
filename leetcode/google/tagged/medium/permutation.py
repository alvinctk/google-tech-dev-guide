from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(Summation of P(N, k))
        The algorithm is faster than O(N * N!), but slower than O(N!).

        P(N, k) := permutation of k elements out of N elements.
        P(N, k) = N!/(N-k)!

        Summation of P(N, k) from k = 1 to k = N  <= Summation of N! from k=1 to k = N.
        O(N!) <= O(Summation of P(N, k) <= O(N * N!)

        Space Complexity: O(N!) since the solution needs to be stored.
        Other non dominant space complexity: O(n) due to recursive depth stack frame

        Runtime: 48 ms, faster than 71.27% of Python3 online submissions for Permutations.
        Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Permutations.
        """
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def helper(permutation, start, end):
            if start == end:
                permutation.append(nums.copy())
                return

            i = start
            while i < end:
                swap(start, i)
                helper(permutation, start + 1, end)
                swap(i, start)
                i += 1

        permutation = []

        helper(permutation, 0, len(nums))
        return permutation


