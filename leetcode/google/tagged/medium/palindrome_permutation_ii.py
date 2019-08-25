"""
Leetcode 267. Palindrome Permutation II
"""
from collections import Counter
from typing import List
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def helper(left, right, path, counter):
            if left >= right:
                result.append("".join(path))

            for k in counter:
                if counter[k] > 0:
                    counter[k] -= 2
                    path[left] = k
                    path[right] = k
                    left += 1
                    right -= 1
                    helper(left, right, path, counter)
                    left -= 1
                    right += 1
                    counter[k] += 2
        if s == 1:
            return [s]

        unique = Counter(s)
        odd = [k for k, v in unique.items() if v % 2 == 1]
        if odd and len(odd) > 1:
            return []
        n = len(s)
        path = [""] * n
        result = []

        if odd:
            unique[odd[0]] -= 1
            path[n//2] = odd[0]


        helper(0, n-1, path, unique)
        return result




