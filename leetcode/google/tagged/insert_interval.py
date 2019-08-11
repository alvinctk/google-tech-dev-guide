from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time complexitiy given without a sorted data:
            Part 1: O(n log n) since algorithm requires a sorted data.
            Part 2: Insert in O(n) given below.
            Hence, time complexity is O(n log n)

        Time complexity given a sorted data:
            Best case: O(n) since either add to the beginning or end
            Average and Worse case: O(n)
        """
        if not intervals:
            return [newInterval]
        elif not newInterval:
            return intervals

        def merge(b, c):
            x_c, y_c = c
            x_b, y_b = b
            if x_b < x_c:
                x_c, y_c = b
                x_b, y_b = c
            if x_c <= x_b and x_b <= y_c:
                return [min(x_c, x_b), max(y_b, y_c)]
            else:
                return None

        x_n, y_n = newInterval
        x_0, y_0 = intervals[0]
        x_l, y_l = intervals[-1]

        output = []
        if x_n > y_l:
            # after end of intervals
            output.extend(intervals)
            output.append(newInterval)
            return output
        elif y_n < x_0:
            # before start of intervals
            output.append(newInterval)
            output.extend(intervals)
            return output

        last = None
        a = None

        # Either merge overlapping new interval
        # or insert disjoint new interval into output
        for i, c in enumerate(intervals):
            m = merge(newInterval, c)
            if not m:
                if output:
                    x_d, y_d = output[-1]
                    x_c, y_c = c
                    # Disjoint interval location found
                    if y_d < x_n and y_n < x_c:
                        output.append(newInterval)
                        output.extend(intervals[i:])
                        return output

                output.append(c)
            else:
                # merge overlapping interval
                a = m
                last = i
                break

        n = len(intervals)
        i = last + 1

        # If merged, check if other intervals needs to merged
        while i < n:
            m = merge(a, intervals[i])
            if not m:
                output.append(a)
                output.extend(intervals[i:])
                break
            else:
                a = m
            i += 1
        else:
            output.append(a)
        return output
