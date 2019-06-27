import shifted_binary_search as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.shiftedBinarySearch([5, 23, 111, 1], 111), 2)

    def test_case_2(self):
        self.assertEqual(program.shiftedBinarySearch([111, 1, 5, 23], 5), 2)

    def test_case_3(self):
        self.assertEqual(program.shiftedBinarySearch([23, 111, 1, 5], 35), -1)

    def test_case_4(self):
        self.assertEqual(program.shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33), 8)

    def test_case_5(self):
        self.assertEqual(program.shiftedBinarySearch([61, 71, 72, 73, 0, 1, 21, 33, 45, 45], 33), 7)

    def test_case_6(self):
        self.assertEqual(program.shiftedBinarySearch([72, 73, 0, 1, 21, 33, 45, 45, 61, 71], 72), 0)

    def test_case_7(self):
        self.assertEqual(program.shiftedBinarySearch([71, 72, 73, 0, 1, 21, 33, 45, 45, 61], 73), 2)

    def test_case_8(self):
        self.assertEqual(program.shiftedBinarySearch([73, 0, 1, 21, 33, 45, 45, 61, 71, 72], 70), -1)

    def test_case_9(self):
        self.assertEqual(program.shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 355), 7)

    def test_case_10(self):
        self.assertEqual(program.shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 354), -1)


if __name__ == "__main__":
    unittest.main()

