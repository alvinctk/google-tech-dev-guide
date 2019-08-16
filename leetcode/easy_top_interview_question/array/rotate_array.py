from typing import List
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead
        Runtime: 68 ms, faster than 93.41% of Python3 online submissions for Rotate Array.
        Memory Usage: 15.2 MB, less than 5.09% of Python3 online submissions for Rotate Array.
        """
        n = len(nums)
        k = k % n
        if not nums or k == 0:
            return

        nums[:] = nums[n-k:] + nums[:n-k]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Reverse approach
        Runtime: 80 ms, faster than 32.90% of Python3 online submissions for Rotate Array.
        Memory Usage: 15.2 MB, less than 5.09% of Python3 online submissions for Rotate Array.
        """
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def reverse_nums(left, right):
            n = len(nums)

            while right < n and left < right:
                swap(left, right)
                left += 1
                right -= 1

        n = len(nums)
        if not nums or k % n == 0:
            return
        k = k % n
        reverse_nums(0, n-1)
        reverse_nums(0, k-1)
        reverse_nums(k, n-1)
        #print(k, w, nums)
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    answer = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    for k in range(6):
        b = nums.copy()
        s.rotate(b, k)
        m = k % len(nums)
        a = answer[m]
        print("i={}, k%n={}, rotate({}, {})={}, answer={}, valid={}".format(k, m, nums, k, b, a, a==b))
