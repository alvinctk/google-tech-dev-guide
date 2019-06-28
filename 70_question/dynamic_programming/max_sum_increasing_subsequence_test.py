import max_sum_increasing_subsequence as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([1]), [1, [1]])

    def test_case_2(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([-1]), [-1, [-1]])

    def test_case_3(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([-1, 1]), [1, [1]])

    def test_case_4(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([5, 4, 3, 2, 1]), [5, [5]])

    def test_case_5(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([1, 2, 3, 4, 5]), [15, [1, 2, 3, 4, 5]])

    def test_case_6(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([-5, -4, -3, -2, -1]), [-1, [-1]])

    def test_case_7(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]), [110, [10, 20, 30, 50]])

    def test_case_8(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]), [35, [8, 12, 15]])

    def test_case_9(self):
        self.assertEqual(program.maxSumIncreasingSubsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]), [164, [10, 11, 14, 23, 25, 31, 50]])


if __name__ == "__main__":
    unittest.main()

