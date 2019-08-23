"""
https://leetcode.com/problems/remove-outermost-parentheses/discuss/364944/Simple-Python-Solution-with-commentary
Add element after the start of the outermost parentheses.

If we set start = 0, we cannot differentiate between the beginning of an outermost parentheses and the ending of outermost parentheses. We need a different number to represent start number that is not zero. That is, start != 0.
start = -1 (It can be any number but not 0)
intialize count = start before the loop
at the beginning we set count to 0 if count == start. This helps to initialize the start of outermost parentheses.
if count != start, then we know that it is somewhere between the start of outermost and the end. So we keep adding to the result.
To keep track of the balancing parentheses count.

count == 0 is when the ")" parenthesis is at the outermost
Add +1 to the count when "("
Add -1 to the count when ")"
Check when iteration reach to the outermost parentheses when count == 0

Then remove the last ")" outer parentheses, since all parentheses are added after the starting parentheses.
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # Runtime: 40 ms, faster than 90.66% of Python3 online submissions for Remove Outermost Parentheses.
        # Memory Usage: 14 MB, less than 5.56% of Python3 online submissions for Remove Outermost Parentheses.
        # Time complexity: O(n)
        # Space complexity: O(n) used list to build result

        result = []
        start = -1
        count = start
        for x in S:

            # Add elements after start
            if count != start:
                result.append(x)
            else:
                count = 0

            # To keep track of balance parentheses
            # count = 0 is when the parentheses is outermost
            if x == "(":
                count += 1
            else:
                count -= 1

            # Only remove the last ")" outermost parentheses
            # Reset count to start
            if count == 0:
                result.pop()
                count = start

        # Return the result
        return "".join(result)
