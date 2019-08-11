from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        92.29% faster than Python3 online submission
        Time complexity: O(n) linear scan
        Space complexity: O(n) use of Counter objects
        """
        if not s and not t:
            return True
        elif not s:
            return False
        elif not t:
            return False

        n, m = len(s), len(t)
        if n != m:
            return False

        a, b = Counter(s), Counter(t)
        for k, v in a.items():
            if a[k] != b[k]:
                return False
        return True
