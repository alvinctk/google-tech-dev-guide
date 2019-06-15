import largest_three_numbers as program
import unittest

class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.findThreeLargestNumbers([55, 7, 8]), [7, 8, 55])

    def test_case_2(self):
        self.assertEqual(program.findThreeLargestNumbers([55, 43, 11, 3, -3, 10]), [11, 43, 55])

    def test_case_3(self):
        self.assertEqual(program.findThreeLargestNumbers([7, 8, 3, 11, 43, 55]), [11, 43, 55])

    def test_case_4(self):
        self.assertEqual(program.findThreeLargestNumbers([55, 7, 8, 3, 43, 11]), [11, 43, 55])

    def test_case_5(self):
        self.assertEqual(program.findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]), [7, 7, 7])

    def test_case_6(self):
        self.assertEqual(program.findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]), [7, 7, 8])

    def test_case_7(self):
        self.assertEqual(program.findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_case_8(self):
        self.assertEqual(program.findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]), [-2, -1, 7])


if __name__ == "__main__":
    unittest.main()
