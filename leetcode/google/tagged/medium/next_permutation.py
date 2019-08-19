from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Runtime: 48 ms, faster than 81.29% of Python3 online submissions for Next Permutation.
        Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Next Permutation.
        """
        if not nums or len(nums) == 1:
            return nums

        n = len(nums)
        k = n - 1

        while k > 0 and nums[k - 1] >= nums[k]:
            k -= 1

        if k == 0:
            nums.sort()
            return

        i, pivot = k, k - 1

        while i < n - 1 and nums[i + 1] > nums[pivot]:
            i += 1

        nums[pivot], nums[i] = nums[i], nums[pivot]

        left, right = k, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

