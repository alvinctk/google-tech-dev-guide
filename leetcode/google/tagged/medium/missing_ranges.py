from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        Time complexity: O(n)
        Runtime beats 91.89% of python3 submission
        """
        if lower > upper:
            return []

        if not nums:
            diff = upper - lower
            if diff == 0:
                return [str(upper)]
            elif diff > 0:
                return [str(lower) + "->" + str(upper)]
            else:
                return []

        def missing_ranges(output, diff, missing_single, missing_lower, missing_upper):
            if diff == 1:
                output.append(str(missing_single))
            else:
                output.append(str(missing_lower) + "->" + str(missing_upper))

        output = [ ]

        start = nums[0]
        if lower < start:
            missing_ranges(output, start - lower, lower, lower, start - 1)

        i, n = 0, len(nums) - 2
        while i <= n:
            diff = nums[i+1] - nums[i]
            if diff == 2:
                missing_ranges(output, 1, nums[i] + 1, None, None)
            elif diff > 2:
                missing_ranges(output, diff, None, nums[i] + 1, nums[i+1] - 1)

            i += 1

        end = nums[-1]
        if end < upper:
            missing_ranges(output, upper - end, upper, end + 1, upper)

        return output
