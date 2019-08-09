import unittest
import find_median_sorted_array as program

class TestProgram(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestProgram, self).__init__(*args, *kwargs)
        self.find_median = program.Solution().findMedianSortedArrays
        self.median = program.Solution().median

    def t(self, x, y, median):
        self.assertEqual(self.find_median(x, y), median)
        self.assertEqual(self.median(x, y), median)

    def test_case1(self):
        self.t([1], [1], 1)
        self.t([2], [1, 3, 4], 2.5)

    def test_case2(self):
        self.t([], [1], 1)
        self.t([1], [], 1)

    def test_case3(self):
        self.t([1], [2, 3], 2)
        self.t([1, 2], [3], 2)
        self.t([1, 3], [2], 2)
        self.t([1, 2], [3, 5], 2.5)

    def test_case4(self):
        self.t([1, 2], [3, 4, 5], 3)
        self.t([1, 3], [2, 4, 5], 3)

    def test_case5(self):
        self.t([2, 7], [3, 4, 5], 4)
        self.t([8, 10], [2, 4, 5], 5)

    def test_case6(self):
        self.t([1], [2, 3, 4, 5, 6], 3.5)
        self.t([2, 3, 4, 5, 6], [1], 3.5)
        self.t([7], [2, 3, 4, 5, 6], 4.5)
        self.t([2, 3, 4, 5, 6], [7], 4.5)

    def test_case7(self):
        self.t([1, 2, 3, 4], [5, 7, 10, 11, 12, 13, 15], 7)
        self.t([4, 5, 8], [1, 2, 3, 4, 5, 7], 4)
        self.t([4, 5, 8], [1, 2, 3, 5, 5, 8], 5)

    def test_case8(self):
        self.t([7, 8], [2, 3, 4, 5, 6], 5)
        self.t([2, 3, 4, 5, 6], [7, 8], 5)

if __name__ == "__main__":
    unittest.main()
