from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Runtime: 32 ms, faster than 96.71% of Python3 online submissions for Longest Palindrome.
        Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Longest Palindrome.
        """
        odd = 0
        for x in set(s):
            if s.count(x) % 2 == 1:
                odd += 1
        return len(s) if odd <= 1 else len(s) - odd + 1

    def longestPalindrome2(self, s: str) -> int:
        """
        Runtime: 36 ms, faster than 84.30% of Python3 online submissions for Longest Palindrome.
        Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Longest Palindrome.
        """
        odd = 0
        for k, v in Counter(s).items():
            if v % 2 == 1:
                odd += 1
        return len(s) if odd <= 1 else len(s) - odd + 1

    def longestPalindrome3(self, s: str) -> int:

        unique = Counter(s)
        odd = [k for k, v in unique.items() if v % 2 == 1]
        if not odd or len(odd) == 1:
            return len(s)
        else:
            return len(s) - len(odd) + 1
