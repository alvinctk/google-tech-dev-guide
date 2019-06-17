import make_change as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.numberOfWaysToMakeChange(0, [2, 3, 4, 7]), 1)

    def test_case_2(self):
        self.assertEqual(program.numberOfWaysToMakeChange(9, [5]), 0)

    def test_case_3(self):
        self.assertEqual(program.numberOfWaysToMakeChange(7, [2, 4]), 0)

    def test_case_4(self):
        self.assertEqual(program.numberOfWaysToMakeChange(6, [1, 5]), 2)

    def test_case_5(self):
        self.assertEqual(program.numberOfWaysToMakeChange(4, [1, 5, 10, 25]), 1)

    def test_case_6(self):
        self.assertEqual(program.numberOfWaysToMakeChange(5, [1, 5, 10, 25]), 2)

    def test_case_7(self):
        self.assertEqual(program.numberOfWaysToMakeChange(10, [1, 5, 10, 25]), 4)

    def test_case_8(self):
        self.assertEqual(program.numberOfWaysToMakeChange(25, [1, 5, 10, 25]), 13)

    def test_case_9(self):
        self.assertEqual(program.numberOfWaysToMakeChange(12, [2, 3, 7]), 4)

    def test_case_10(self):
        self.assertEqual(program.numberOfWaysToMakeChange(7, [2, 3, 4, 7]), 3)

    def test_case_11(self):
        self.assertEqual(program.numberOfWaysToMakeChange(6, [1, 5]), 2)




if __name__ == "__main__":
    unittest.main()

