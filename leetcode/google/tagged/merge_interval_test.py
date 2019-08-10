import unittest
import merge_interval as program

class IntervalTestCase(unittest.TestCase):
    """
    Base class for all interval tests
    """
    def setUp(self):
        self.merge_intervals = program.Solution().merge

    def assertIntervalEqual(self, intervals, value):
        self.assertEqual(self.merge_intervals(intervals), value)


class TestProgram(IntervalTestCase):
    def test_empty(self):
        self.assertIntervalEqual([], [])

    def test_no_merge(self):
        self.assertIntervalEqual([[1, 1], [2, 2]], [[1, 1], [2, 2]])
        self.assertIntervalEqual([[1, 3], [6, 10]], [[1, 3], [6, 10]])

    def test_all_merge(self):
        self.assertIntervalEqual([[1, 2], [2, 4]], [[1, 4]])
        self.assertIntervalEqual([[1, 2], [1, 5], [1, 3], [1, 10]], [[1, 10]])
        self.assertIntervalEqual([[1, 2], [2, 5], [1, 7], [6, 10]], [[1, 10]])

    def test_combination_merge(self):
        self.assertIntervalEqual([[1, 2], [2, 4], [11, 38]], [[1, 4], [11, 38]])
        self.assertIntervalEqual([[1, 2], [33, 88], [1, 3], [3, 10]], [[1, 10], [33, 88]])


if __name__ == "__main__":
    unittest.main()
