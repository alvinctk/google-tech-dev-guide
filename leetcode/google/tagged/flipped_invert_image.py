from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """
        56ms, faster than 92.39% of Python3 submission
        13.7 MB less than 5.11% of Python3 submission
        """
        return [list(map(lambda x: 0 if x else 1, row[::-1])) for row in A]


    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """
        60ms, faster than 74.21% of Python3 submission
        13.8 MB less than 5.11% of Python3 submission
        """
        return [[1- x for x in reversed(row)] for row in A]

    def flipAndInvertImage2(self, A: List[List[int]]) -> List[List[int]]:
        """
        76 ms faster than 13.91% of Python3 online submission
        13.5MB less than 5.11% of Python3 submission
        """
        def invert(x):
            if x:
                return 0
            else:
                return 1

        for row in A:
            left, right = 0, len(row)-1
            while left <= right:
                row[left], row[right] = invert(row[right]), invert(row[left])
                left += 1
                right -= 1

        return A



