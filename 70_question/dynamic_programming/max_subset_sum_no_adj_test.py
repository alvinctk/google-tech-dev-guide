import max_subset_sum_no_adj as program
import unittest

class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([]), 0)

    def test_case_2(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([1]), 1)

    def test_case_3(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([1, 2]), 2)

    def test_case_4(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([1, 2, 3]), 4)

    def test_case_5(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([1, 15, 3]), 15)

    def test_case_6(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]), 33)

    def test_case_7(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([4, 3, 5, 200, 5, 3]), 207)

    def test_case_8(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([10, 5, 20, 25, 15, 5, 5, 15]), 60)

    def test_case_9(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15]), 90)

    def test_case_10(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([125, 210, 250, 120, 150, 300]), 675)

    def test_case_11(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([30, 25, 50, 55, 100]), 180)

    def test_case_12(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([30, 25, 50, 55, 100, 120]), 205)

    def test_case_13(self):
        self.assertEqual(program.maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4]), 72)


if __name__ == "__main__":
    unittest.main()

