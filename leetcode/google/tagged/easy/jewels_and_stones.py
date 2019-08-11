from typing import List

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        98.84% faster than Python3 submission
        Time complexity: O(n)
            O(n) for iterating each stones
            O(1) for checking if a stone is a jewel by using a set

        Space complexity: O(n) for creating a hashable set for quick comparsion
        """
        jewels = set(J)
        count = 0
        for stone in S:
            if stone in jewels:
                count += 1
        return count

    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        9% faster than python3 submission
        """
        return sum(map(S.count, set(J)))

    def numcJewelsInStones(self, J: str, S: str) -> int:
        """
        6.73% faster
        """
        return len([stone for stone in S if stone in set(J)])
