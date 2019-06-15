import unittest
from two_number_sum import twoNumberSum_0 as a
from two_number_sum import twoNumberSum_1 as b
from two_number_sum import twoNumberSum_2 as c

class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(a([4, 6], 10), [4, 6])
        self.assertEqual(b([4, 6], 10), [4, 6])
        self.assertEqual(c([4, 6], 10), [4, 6])

if __name__ == "__main__":
    unittest.main()
