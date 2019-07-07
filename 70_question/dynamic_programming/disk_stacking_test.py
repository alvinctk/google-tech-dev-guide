import disk_stacking as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.diskStacking([[2, 1, 2]]), [[2, 1, 2]])

    def test_case_2(self):
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3]]), [[2, 1, 2], [3, 2, 3]])

    def test_case_3(self):
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]]), [[2, 2, 8]])

    def test_case_4(self):
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 3, 4]]), [[2, 1, 2], [3, 2, 3]])

    def test_case_5(self):
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]), [[2, 1, 2], [3, 2, 3], [4, 4, 5]])

    def test_case_6(self):
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 5], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]), [[2, 3, 4], [4, 4, 5]])

    def test_case_7(self):
        self.assertEqual(program.diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5], [1, 1, 4]]), [[1, 1, 4], [2, 2, 8]])

    def test_case_8(self):
        self.assertEqual(program.diskStacking([[3, 3, 4], [2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [5, 5, 6], [1, 2, 1], [4, 4, 5], [1, 1, 4], [2, 2, 3]]), [[2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6]])


if __name__ == "__main__":
    unittest.main()

