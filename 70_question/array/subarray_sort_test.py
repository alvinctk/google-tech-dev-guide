import subarray_sort as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.subarraySort([1, 2]), [-1, -1])

    def test_case_2(self):
        self.assertEqual(program.subarraySort([2, 1]), [0, 1])

    def test_case_3(self):
        self.assertEqual(program.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test_case_4(self):
        self.assertEqual(program.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]), [4, 9])

    def test_case_5(self):
        self.assertEqual(program.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]), [4, 6])

    def test_case_6(self):
        self.assertEqual(program.subarraySort([1, 2, 8, 4, 5]), [2, 4])

    def test_case_7(self):
        self.assertEqual(program.subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]), [0, 12])

    def test_case_8(self):
        self.assertEqual(program.subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]), [0, 11])

    def test_case_9(self):
        self.assertEqual(program.subarraySort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]), [1, 11])

    def test_case_10(self):
        self.assertEqual(program.subarraySort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]), [1, 12])

    def test_case_11(self):
        self.assertEqual(program.subarraySort([1, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11]), [6, 7])

    def test_case_12(self):
        self.assertEqual(program.subarraySort([1, 2, 3, 4, 5, 6, 18, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19]), [6, 16])

    def test_case_13(self):
        self.assertEqual(program.subarraySort([1, 2, 3, 4, 5, 6, 18, 21, 22, 7, 14, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 4, 14, 11, 6, 33, 35, 41, 55]), [4, 24])

    def test_case_14(self):
        self.assertEqual(program.subarraySort([1, 2, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), [2, 19])

    def test_case_15(self):
        self.assertEqual(program.subarraySort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2]), [2, 19])

    def test_case_16(self):
        self.assertEqual(program.subarraySort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), [-1, -1])

    def test_case_17(self):
        self.assertEqual(program.subarraySort([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]), [-1, -1])

    def test_case_18(self):
        self.assertEqual(program.subarraySort([]), [-1, -1])
        self.assertEqual(program.subarraySort([1]), [-1, -1])
        self.assertEqual(program.subarraySort([1, 2]), [-1, -1])

    def test_case_19(self):
        self.assertEqual(program.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])
        self.assertEqual(program.subarraySort([1, 2, 4, 5, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [4, 9])

    def test_case_20(self):
        self.assertEqual(program.subarraySort([7, 8, 8, 9, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [0, 9])
        self.assertEqual(program.subarraySort([6, 8, 8, 9, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [1, 9])
        self.assertEqual(program.subarraySort([1, 2, 4, 5, 10, 11, 7, 12, 6, 7, 10, 11, 12]), [4, 11])
        self.assertEqual(program.subarraySort([7, 8, 8, 9, 10, 11, 7, 12, 6, 7, 11, 12, 12]), [0, 10])
        self.assertEqual(program.subarraySort([7, 8, 8, 9, 10, 11, 7, 12, 6, 7, 11, 11, 11]), [0, 12])

if __name__ == "__main__":
    unittest.main()

