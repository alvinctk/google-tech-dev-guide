import max_profit_with_k_transactions as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.maxProfitWithKTransactions([], 1), 0)

    def test_case_2(self):
        self.assertEqual(program.maxProfitWithKTransactions([1], 1), 0)

    def test_case_3(self):
        self.assertEqual(program.maxProfitWithKTransactions([1, 10], 1), 9)

    def test_case_4(self):
        self.assertEqual(program.maxProfitWithKTransactions([1, 10], 3), 9)

    def test_case_5(self):
        self.assertEqual(program.maxProfitWithKTransactions([3, 2, 5, 7, 1, 3, 7], 1), 6)

    def test_case_6(self):
        self.assertEqual(program.maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2), 93)

    def test_case_7(self):
        self.assertEqual(program.maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 3), 93)

    def test_case_8(self):
        self.assertEqual(program.maxProfitWithKTransactions([5, 11, 3, 50, 40, 90], 2), 97)

    def test_case_9(self):
        self.assertEqual(program.maxProfitWithKTransactions([5, 11, 3, 50, 40, 90], 3), 103)

    def test_case_10(self):
        self.assertEqual(program.maxProfitWithKTransactions([50, 25, 12, 4, 3, 10, 1, 100], 2), 106)

    def test_case_11(self):
        self.assertEqual(program.maxProfitWithKTransactions([100, 99, 98, 97, 1], 5), 0)

    def test_case_12(self):
        self.assertEqual(program.maxProfitWithKTransactions([1, 100, 2, 200, 3, 300, 4, 400, 5, 500], 5), 1485)

    def test_case_13(self):
        self.assertEqual(program.maxProfitWithKTransactions([1, 100, 101, 200, 201, 300, 301, 400, 401, 500], 5), 499)

    def test_case_14(self):
        self.assertEqual(program.maxProfitWithKTransactions([1, 25, 24, 23, 12, 36, 14, 40, 31, 41, 5], 4), 84)

    def test_case_15(self):
        self.assertEqual(program.maxProfitWithKTransactions([1, 25, 24, 23, 12, 36, 14, 40, 31, 41, 5], 2), 62)


if __name__ == "__main__":
    unittest.main()

