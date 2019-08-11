import unittest
import insert_interval as program
class IntervalTestCase(unittest.TestCase):
    def setUp(self):
        self.insert_intervals = program.Solution().insert

    def assertIntervalEqual(self, intervals, new_interval, value):
        self.assertEqual(self.insert_intervals(intervals, new_interval), value)

class TestProgram(IntervalTestCase):
    def test_leetcode(self):
        self.assertIntervalEqual([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
        self.assertIntervalEqual([[6, 9]], [2, 5], [[2, 5], [6, 9]])
        self.assertIntervalEqual([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
        self.assertIntervalEqual([], [1, 4], [[1, 4]])

        self.assertIntervalEqual([[1,3],[6,9]], [2,5], [[1,5],[6,9]])
        self.assertIntervalEqual([], [2 ,5], [[2, 5]])
        self.assertIntervalEqual([[5, 6], [7, 9]], [6, 8], [[5, 9]])
        self.assertIntervalEqual([[5, 6]], [1, 2], [[1, 2], [5, 6]])
        self.assertIntervalEqual([[3, 10], [11, 34]], [1, 5], [[1, 10], [11, 34]])
        self.assertIntervalEqual([[3, 5]], [1, 10], [[1, 10]])

    def test_non_overlap(self):
        self.assertIntervalEqual([[1, 8], [11, 12]], [9, 10], [[1, 8], [9, 10], [11, 12]])
        self.assertIntervalEqual([[1, 8], [11, 12]], [14, 16], [[1, 8], [11, 12], [14, 16]])
        self.assertIntervalEqual([[1, 4], [7, 8], [11, 35]], [9, 10], [[1, 4], [7, 8], [9, 10], [11, 35]])

    def test_empty(self):
        self.assertIntervalEqual([], [], [[]])
        self.assertIntervalEqual([[1, 2]], [], [[1, 2]])
        self.assertIntervalEqual([], [1, 2], [[1, 2]])
        self.assertIntervalEqual([], [1, 4], [[1, 4]])

    def test_contains_midl(self):
        self.assertIntervalEqual([[3, 5]], [1, 10], [[1, 10]])
        self.assertIntervalEqual([[3, 5], [7, 11]], [1, 10], [[1, 11]])

    def test_first_interval(self):
        self.assertIntervalEqual([[3, 5]], [0, 1], [[0, 1], [3, 5]])
        self.assertIntervalEqual([[3, 5], [6, 7]], [0, 1], [[0, 1], [3, 5], [6, 7]])

    def test_last_interval(self):
        self.assertIntervalEqual([[3, 5]], [6, 7], [[3, 5], [6, 7]])
        self.assertIntervalEqual([[3, 5], [6, 7]], [8, 9], [[3, 5], [6, 7], [8, 9]])

    def test_mid_interval(self):
        self.assertIntervalEqual([[3, 5], [6, 9], [11, 23], [44, 99]], [10, 11], [[3, 5], [6, 9], [10, 23], [44, 99]])
        self.assertIntervalEqual([[3, 5], [6, 9], [11, 23], [44, 99]], [11, 100], [[3, 5], [6, 9], [11, 100]])
        self.assertIntervalEqual([[3, 5], [6, 9], [11, 23], [44, 99]], [1, 100], [[1, 100]])


if __name__ == "__main__":
    unittest.main()
