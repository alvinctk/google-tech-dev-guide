import min_jumps as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.minNumberOfJumps([1]), 0)

    def test_case_2(self):
        self.assertEqual(program.minNumberOfJumps([1, 1]), 1)

    def test_case_3(self):
        self.assertEqual(program.minNumberOfJumps([3, 1]), 1)

    def test_case_4(self):
        self.assertEqual(program.minNumberOfJumps([1, 1, 1]), 2)

    def test_case_5(self):
        self.assertEqual(program.minNumberOfJumps([2, 1, 1]), 1)

    def test_case_6(self):
        self.assertEqual(program.minNumberOfJumps([2, 1, 2, 3, 1]), 2)

    def test_case_7(self):
        self.assertEqual(program.minNumberOfJumps([2, 1, 2, 3, 1, 1, 1]), 3)

    def test_case_8(self):
        self.assertEqual(program.minNumberOfJumps([2, 1, 2, 2, 1, 1, 1]), 4)

    def test_case_9(self):
        self.assertEqual(program.minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)

    def test_case_10(self):
        self.assertEqual(program.minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 6, 2, 1, 1, 1, 1]), 5)

    def test_case_11(self):
        self.assertEqual(program.minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 7)

    def test_case_12(self):
        self.assertEqual(program.minNumberOfJumps([3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 6)

    def test_case_13(self):
        self.assertEqual(program.minNumberOfJumps([3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 5)

    def test_case_14(self):
        self.assertEqual(program.minNumberOfJumps([3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()

