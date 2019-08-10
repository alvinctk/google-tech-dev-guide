from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(n)
        Runtime beats 97.84 % of python3 submissions.
        """
        if not intervals or len(intervals) < 2:
            return intervals

        output = []
        intervals.sort(key = lambda x: x[0])

        a = intervals[0]
        n = len(intervals)

        for i, b in enumerate(intervals[1:]):
            x_a, y_a = a
            x_b, y_b = b
            if x_a <= x_b and x_b <= y_a:
                a = [x_a, max(y_a, y_b)]
            else:
                output.append(a)
                a = b

        # Either len(intervals) == 2 and output is none due to two intervals meged into one
        # Or the last input
        if not output or output[-1] != a:
            output.append(a)

        return output

