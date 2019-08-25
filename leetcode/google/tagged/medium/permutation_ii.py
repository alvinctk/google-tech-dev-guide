from collections import Counter
class Solution:
    def permuteUnique(self, nums):
        """
        Time complexity: (N - w) * O(Summation of P(N-w, k))
            w = number of duplicate elements
            P(N - w, k) := permutation of unique elements of k from N - w elements
            P(N - w, k) = (N-w)!/(N-w-k)!

        Space complexity: O((N-w)!) to store result
        """
        def helper(path, counter):
            if len(path) == len(nums):
                result.append(path.copy())

            for x in counter:  # dont pick duplicates
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1

                    helper(path, counter)
                    path.pop()
                    counter[x] += 1
        result = []
        helper([], Counter(nums))
        return result
