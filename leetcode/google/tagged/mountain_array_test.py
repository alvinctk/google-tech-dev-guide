import unittest
import mountain_array as program

class TestProgram(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestProgram, self).__init__(*args, **kwargs)
        self.mountain = program.Solution().validMountainArray

    def t(self, A, value):
        self.assertEqual(self.mountain(A), value)

    def test_case1(self):
        self.t([3, 5, 5], False)
        self.t([3, 5, 5, 6], False)
        self.t([4, 4, 1], False)
        self.t([5, 4, 1], False)

    def test_case3(self):
        self.t([1], False)
        self.t([1, 2], False)
        self.t([3, 1], False)
        self.t([3, 3, 3], False)
        self.t([3, 3, 3, 3, 3], False)
        self.t([3, 3, 3, 3, 3, 3], False)
        self.t([3, 3, 3, 3, 3, 3], False)
        self.t([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False)
        self.t([0, 3, 4, 5, 6, 7, 8, 9], False)

    def test_case2(self):
        self.t([1, 2, 3, 5, 4, 3, 1], True)
        self.t([1, 2, 3, 5, 4], True)
        self.t([0, 3, 2, 1], True)
        self.t([0, 3, 2], True)

    def test_case4(self):
        self.t([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], False)

    def test_case5(self):
        self.t([3, 7, 6, 4, 0, 1, 0], False)


if __name__ == "__main__":
    unittest.main()
