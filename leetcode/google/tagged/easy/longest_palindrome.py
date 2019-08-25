from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:

        unique = Counter(s)
        odd = [k for k, v in unique.items() if v % 2 == 1]
        if not odd or len(odd) == 1:
            return len(s)
        else:
            return len(s) - len(odd) + 1
