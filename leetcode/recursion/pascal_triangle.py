from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(output, n):
            """
            practice recursion to generate pascal triangle
            """
            if n > numRows:
                return output
            elif n == 1:
                output.append([1])
            elif n == 2:
                output.append([1, 1])
            else:
                m, previous = len(output[-1]), output[-1]
                array = [0] * (m + 1)
                array[0], array[-1] = previous[0], previous[-1]

                left, right = 0, 1
                while left != m - 1:
                    array[right] = previous[left] + previous[right]
                    left += 1
                    right += 1

                output.append(array)

            return helper(output, n+1)

        return helper([], 1)

    def generate_iteration(self, numRows: int) -> List[List[int]]:
        def helper(output):
            """
            iterative helper to generate pascal triangle
            """
            m, previous = len(output[-1]), output[-1]
            array = [0] * (m + 1)
            array[0], array[-1] = previous[0], previous[-1]

            left, right = 0, 1
            while left != m - 1:
                array[right] = previous[left] + previous[right]
                left += 1
                right += 1

            output.append(array)

        output = []
        if numRows >= 1: output.append([1])
        if numRows >= 2: output.append([1, 1])
        i = 3
        while i < numRows+1:
            helper(output)
            i += 1
        return output

if __name__ == "__main__":
    x = Solution()
    print(x.generate(5))
    print(x.generate_iteration(5))
    print(x.generate_iteration(8))
