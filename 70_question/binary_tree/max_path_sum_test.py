from max_path_sum import max_path_sum
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3])
        self.assertEqual(max_path_sum(test), 6)

    def test_case_2(self):
        test = BinaryTree(1).insert([2, -1])
        self.assertEqual(max_path_sum(test), 3)

    def test_case_3(self):
        test = BinaryTree(1).insert([-5, 3, 6])
        self.assertEqual(max_path_sum(test), 6)

    def test_case_4(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(max_path_sum(test), 18)

    def test_case_5(self):
        test = BinaryTree(1).insert([-10, -5, 30, 45, -20, -21, 5, 1, 3, -3, 100, 2, 100, 1])
        self.assertEqual(max_path_sum(test), 154)

    def test_case_6(self):
        test = BinaryTree(1).insert([-10, -5, 30, 45, -20, -21, 5, 1, 3, -3, 100, 2, 100, 1, 100])
        self.assertEqual(max_path_sum(test), 201)

    def test_case_7(self):
        test = BinaryTree(1).insert([-10, -5, 30, 75, -20, -21, 5, 1, 3, -3, 100, 2, 100, 1, 100])
        self.assertEqual(max_path_sum(test), 203)

    def test_case_8(self):
        test = BinaryTree(1).insert([-150, -5, 30, 75, -20, -21, 5, 1, 3, -3, 100, 2, 100, 1, 100, 100, 5, 10, 150, -8])
        self.assertEqual(max_path_sum(test), 228)

    def test_case_9(self):
        test = BinaryTree(1).insert([-150, -5, 30, 75, -20, -21, 5, 1, 3, -3, 100, 2, 100, 1, 100, 100, 5, 10, 150, 151])
        self.assertEqual(max_path_sum(test), 304)

    def test_case_10(self):
        test = BinaryTree(1).insert([-5, -3, 0, 2, 2, 1, -3, 3, 1, 1, 0, 5, 1, 1, 0, 1, 1, -1, -1, -6, -1, -100, -9, -91, 2, 1, 0, 1, -5, 0])
        self.assertEqual(max_path_sum(test), 9)

    def test_case_11(self):
        test = BinaryTree(1).insert([-5, -3, 0, 2, 2, 1, -3, -4, 1, 1, 0, 5, 1, 1, 0, 1, 10, -1, -1, -6, -1, -100, -9, -91, 2, 1, 0, 1, -5, 0])
        self.assertEqual(max_path_sum(test), 10)

    def test_case_12(self):
        test = BinaryTree(1).insert([-5, -3, 0, 2, 2, 1, -3, -4, 1, 1, 0, 5, 1, 1, 0, 1, 3, -1, -1, -6, -1, -100, -9, -91, 2, 1, 0, 1, -5, 0, 3, 1, 2, 2, 7, -5])
        self.assertEqual(max_path_sum(test), 10)

    def test_case_13(self):
        test = BinaryTree(1).insert([-5, -3, 0, 2, 2, 1, -3, 3, 1, 1, 0, 5, 1, 1, 0, 1, 1, -1, -1, -6, -1, -100, -9, -91, 2, 1, 0, 1, 5, 0])
        self.assertEqual(max_path_sum(test), 13)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i = 0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


if __name__ == "__main__":
	unittest.main()
