class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply_single(array, x):
            print(array, x)
            overflow = 0
            k = 0
            num = 0
            for y in reversed(array):
                total = y * x + overflow
                overflow = total // 10
                num += total % 10 * 10 ** k
                k += 1
            if overflow:
                num += overflow * 10 ** k
            return num

        num1 = [int(x) for x in num1]
        num2 = [int(y) for y in num2]
        k = 0
        num = 0
        for y in reversed(num2):
            total = multiply_single(num1, y)
            num += total * 10 ** k
            k += 1
        return num

if __name__ == "___main__":
    num1 = "6"
    num2 = "2"
    x = Solution()
    x.multiply(num1, num2)

