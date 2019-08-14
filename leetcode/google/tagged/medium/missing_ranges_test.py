import unittest
import missing_ranges as program

class TestCase(unittest.TestCase):
    def setUp(self):
        self.missing_range = program.Solution().findMissingRanges
        self.t = self.assertMissingRange

    def assertMissingRange(self, ranges, lower, upper, answer):
        self.assertEqual(self.missing_range(ranges, lower, upper), answer)

class TestProgram(TestCase):
    def test_example(self):
        self.t([0,1,3,50,75], 0, 99, ["2","4->49","51->74","76->99"])

    def test_empty(self):
        self.t([], 4, -1, [])
        self.t([], 1, 1, ["1"])
        self.t([], -1, -1, ["-1"])
        self.t([], 0, 100, ["0->100"])
        self.t([], -1, 100, ["-1->100"])
        self.t([], -100, 100, ["-100->100"])
        self.t([], -100, 0, ["-100->0"])

    def test_repeat(self):
        self.t([1, 1, 1], 0, 100, ["0", "2->100"])
        self.t([1, 1, 1, 1, 1, 1, 1, 1, 1], 0, 100, ["0", "2->100"])


    def test_single(self):
        self.t([1, 3, 5, 7, 8, 9, 10], 0, 11, ["0", "2", "4", "6", "11"])

    def test_missing_negative_range(self):
        self.t([-990,-800,-701,-60, -5], -999, -1, ["-999->-991", "-989->-801", "-799->-702", "-700->-61", "-59->-6", "-4->-1"])
        self.t([-990,-800,-701,-60, -5], -991, -1, ["-991", "-989->-801", "-799->-702", "-700->-61", "-59->-6", "-4->-1"])
        self.t([-990,-800,-701,-60, -5], -991, -4, ["-991", "-989->-801", "-799->-702", "-700->-61", "-59->-6", "-4"])

    def test_missing_start(self):
        self.t([-1,1,3,50,100], -6, 100, ["-6->-2","0","2","4->49","51->99"])
        self.t([-1,1,3,50,100], -2, 100, ["-2","0","2","4->49","51->99"])
        self.t([1,3,50,100], 0, 100, ["0","2","4->49","51->99"])
        self.t([50,100], 0, 100, ["0->49", "51->99"])

    def test_missing_start_and_end(self):
        self.t([-6,1,3,50,100, 101], -6, 102, ["-5->0","2","4->49","51->99", "102"])
        self.t([-6,0,3,50,100, 101], -6, 102, ["-5->-1","1->2","4->49","51->99", "102"])
        self.t([-4,0,3,50,100, 101], -99, 102, ["-99->-5", "-3->-1","1->2","4->49","51->99", "102"])
        self.t([-4,0,3,50,100, 101], -99, 999, ["-99->-5", "-3->-1","1->2","4->49","51->99", "102->999"])

    def test_missing_end(self):
        self.t([0,1,3,50,100, 101], 0, 300, ["2","4->49","51->99", "102->300"])

if __name__ == "__main__":
    unittest.main()
