class Solution(object):
    def decodeString(self, s):
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


