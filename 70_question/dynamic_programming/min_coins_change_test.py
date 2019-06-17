import min_coins_change as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.minNumberOfCoinsForChange(0, [1, 2, 3]), 0)

    def test_case_2(self):
        self.assertEqual(program.minNumberOfCoinsForChange(3, [2, 1]), 2)

    def test_case_3(self):
        self.assertEqual(program.minNumberOfCoinsForChange(4, [1, 5, 10]), 4)

    def test_case_4(self):
        self.assertEqual(program.minNumberOfCoinsForChange(7, [1, 5, 10]), 3)

    def test_case_5(self):
        self.assertEqual(program.minNumberOfCoinsForChange(10, [1, 5, 10]), 1)

    def test_case_6(self):
        self.assertEqual(program.minNumberOfCoinsForChange(11, [1, 5, 10]), 2)

    def test_case_7(self):
        self.assertEqual(program.minNumberOfCoinsForChange(24, [1, 5, 10]), 6)

    def test_case_8(self):
        self.assertEqual(program.minNumberOfCoinsForChange(25, [1, 5, 10]), 3)

    def test_case_9(self):
        self.assertEqual(program.minNumberOfCoinsForChange(7, [2, 4]), -1)

    def test_case_10(self):
        self.assertEqual(program.minNumberOfCoinsForChange(7, [3, 7]), 1)

    def test_case_11(self):
        self.assertEqual(program.minNumberOfCoinsForChange(9, [3, 5]), 3)

    def test_case_12(self):
        self.assertEqual(program.minNumberOfCoinsForChange(9, [3, 4, 5]), 2)

    def test_case_13(self):
        self.assertEqual(program.minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1]), 3)

    def test_case_14(self):
        self.assertEqual(program.minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]), 2)


if __name__ == "__main__":
    unittest.main()

