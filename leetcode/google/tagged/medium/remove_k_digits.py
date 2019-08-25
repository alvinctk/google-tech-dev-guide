class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k <= 0:
            return num
        elif not num or len(num) - k  == 0:
            return "0"
        debug = False
        stack = []
        remove = []
        i, n = 0, len(num)
        total = n - k

        while i < n:
            if debug: print("i={} k={} num[{}]={} stack={} remove={}".format(i, k, i, num[i], stack, remove))
            if not stack:
                if num[i] == "0":
                    k -= 1
                    remove.append("0")
                else:
                    stack.append(num[i])
                i += 1
                continue

            if stack[-1] > num[i]:
                if k > 0:
                    k -= 1
                    remove.append(stack.pop())
                    # don't count k for non-leading zeros
                    while not stack and i < n and num[i] == "0":
                        i += 1
                    continue
                else:
                    stack.append(num[i])
                    i += 1
            elif stack[-1] < num[i]:
                if len(stack) < total:
                    stack.append(num[i])
                i += 1

            else:
                stack.append(num[i])
                i += 1

        while stack and len(stack) > total:
            if debug: print("stack={}".format(stack))
            stack.pop()

        return "".join(stack) if stack else "0"
