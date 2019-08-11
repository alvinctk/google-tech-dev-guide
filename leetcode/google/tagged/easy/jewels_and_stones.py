from typing import List

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        76% faster than python3 submission
        """
        return sum(map(S.count, set(J)))

    def numcJewelsInStones(self, J: str, S: str) -> int:
        """
        6.73% faster
        """
        return len([stone for stone in S if stone in set(J)])
