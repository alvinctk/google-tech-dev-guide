class Solution(object):
    def decodeString(self, s):
        """
        Time complexity: O(N) linear scan through all elements of s
        Space complexity: O(N) to store auxillary data
        Runtime: 28 ms, faster than 97.19% of Python3 online submissions for Decode String.
        Memory Usage: 13.8 MB, less than 5.77% of Python3 online submissions for Decode String.
        """

        stack = []
        multiply = 0
        current = []
        for x in s:
            if x == "[":
                stack.append("".join(current))
                stack.append(multiply)
                current = []
                multiply = 0
            elif x == "]":
                times = stack.pop()
                previous = stack.pop()
                current = [previous + "".join(current) * times]
            elif x.isdigit():
                multiply = multiply * 10 + int(x)
            else:
                current.append(x)

            print(stack, current)
        return "".join(current)


