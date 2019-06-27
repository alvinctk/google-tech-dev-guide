import quick_select as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.quickselect([1], 1), 1)

    def test_case_2(self):
        self.assertEqual(program.quickselect([43, 24, 37], 1), 24)

    def test_case_3(self):
        self.assertEqual(program.quickselect([43, 24, 37], 2), 37)

    def test_case_4(self):
        self.assertEqual(program.quickselect([43, 24, 37], 3), 43)

    def test_case_5(self):
        self.assertEqual(program.quickselect([8, 5, 2, 9, 7, 6, 3], 3), 5)

    def test_case_6(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 1), 1)

    def test_case_7(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 2), 2)

    def test_case_8(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 3), 3)

    def test_case_9(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 4), 4)

    def test_case_10(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 5), 5)

    def test_case_11(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 6), 6)

    def test_case_12(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 7), 7)

    def test_case_13(self):
        self.assertEqual(program.quickselect([8, 3, 2, 5, 1, 7, 4, 6], 8), 8)

    def test_case_14(self):
        self.assertEqual(program.quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5), 25)
        self.assertEqual(program.quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5), 25)

    def test_case_15(self):
        self.assertEqual(program.quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 4), 15)

    def test_case_16(self):
        self.assertEqual(program.quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 9), 102)

    def test_case_17(self):
        self.assertEqual(program.quickselect([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151125], 12), 55516151125)

    def test_case_18(self):
        self.assertEqual(program.quickselect([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151125], 4), 123)


if __name__ == "__main__":
    unittest.main()

