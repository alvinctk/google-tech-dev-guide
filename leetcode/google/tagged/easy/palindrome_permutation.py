"""
Leetcode 266. Palindrome Permutation
"""
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        unique = Counter(s)
        odd = [k for k, v in unique.items() if v % 2 == 1]
        if odd and len(odd) > 1:
            return False
        else:
            return True
