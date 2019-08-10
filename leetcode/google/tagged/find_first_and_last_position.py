from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

        Time complexity: O(log n) since binary search algorithm is used.
        Binary search algorithm cuts the search space roughly in half on each iteration.

        Space complexity: O(1) since all work are done in place.

        Runtime beats 92.59% of python3 submission
        """
        if not nums:
            return [-1, -1]
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start + 1 + 1)//2 - 1
            left = right = -1
            if nums[mid] == target:
                left = right = mid
            elif nums[start] == target:
                left = right = start
            elif nums[end] == target:
                left = right = end

            if 0 <= left and left < n:
                has_left = left - 1 >= 0 and nums[left-1] == target
                has_right = right + 1 < n and nums[right+1] == target
                while has_left or has_right:
                    if has_left:
                        left -= 1
                    if has_right:
                        right += 1
                    has_left = left - 1 >= 0 and nums[left-1] == target
                    has_right = right + 1 < n and nums[right+1] == target

                return [left, right]

            elif nums[mid] > target:
                # [0, mid - 1]
                end = mid - 1
            else:
                # [mid + 1, n]
                start = mid + 1

        return [-1, -1]

if __name__ == "__main__":
    s = Solution()
    numbers = [[1, 2, 3, 4, 5, 6, 7, 9, 10], [1, 2, 3, 3, 4, 5, 6], [5, 7, 7, 8, 8, 10], [5, 7, 8, 8, 10], [1, 1], [1, 1], []]
    for x in numbers:
        for i in range(11):
            r = s.searchRange(x, i)
            print("searchRange({}, {}) = {}".format(x, i, r))
