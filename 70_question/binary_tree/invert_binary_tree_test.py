from invert_binary_tree import invert_binary_tree
import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

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

    def invertedInsert(self, values, i = 0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self

test1 = BinaryTree(1)
invertedTest1 = BinaryTree(1)

test2 = BinaryTree(1).insert([2])
invertedTest2 = BinaryTree(1).invertedInsert([2])

test3 = BinaryTree(1).insert([2, 3])
invertedTest3 = BinaryTree(1).invertedInsert([2, 3])

test4 = BinaryTree(1).insert([2, 3, 4])
invertedTest4 = BinaryTree(1).invertedInsert([2, 3, 4])

test5 = BinaryTree(1).insert([2, 3, 4, 5])
invertedTest5 = BinaryTree(1).invertedInsert([2, 3, 4, 5])

test6 = BinaryTree(1).insert([2, 3, 4, 5, 6])
invertedTest6 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6])

test7 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
invertedTest7 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7])

test8 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8])
invertedTest8 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8])

test9 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
invertedTest9 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])

test10 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
invertedTest10 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9, 10])

test11 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
invertedTest11 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        invert_binary_tree(test1)
        self.assertTrue(test1, invertedTest1)

    def test_case_2(self):
        invert_binary_tree(test2)
        self.assertTrue(test2.__eq__(invertedTest2))

    def test_case_3(self):
        invert_binary_tree(test3)
        self.assertTrue(test3.__eq__(invertedTest3))

    def test_case_4(self):
        invert_binary_tree(test4)
        self.assertTrue(test4.__eq__(invertedTest4))

    def test_case_5(self):
        invert_binary_tree(test5)
        self.assertTrue(test5.__eq__(invertedTest5))

    def test_case_6(self):
        invert_binary_tree(test6)
        self.assertTrue(test6.__eq__(invertedTest6))

    def test_case_7(self):
        invert_binary_tree(test7)
        self.assertTrue(test7.__eq__(invertedTest7))

    def test_case_8(self):
        invert_binary_tree(test8)
        self.assertTrue(test8.__eq__(invertedTest8))

    def test_case_9(self):
        invert_binary_tree(test9)
        self.assertTrue(test9.__eq__(invertedTest9))

    def test_case_10(self):
        invert_binary_tree(test10)
        self.assertTrue(test10.__eq__(invertedTest10))

    def test_case_11(self):
        invert_binary_tree(test11)
        self.assertTrue(test11.__eq__(invertedTest11))


if __name__ == "__main__":
    unittest.main()
