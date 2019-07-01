import lcm as program
import unittest


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)

orgCharts = {}
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for letter in ALPHABET:
    orgCharts[letter] = OrgChart(letter)
orgCharts['A'].addDirectReports([
    orgCharts['B'],
    orgCharts['C'],
    orgCharts['D'],
    orgCharts['E'],
    orgCharts['F'],
])
orgCharts['B'].addDirectReports([
    orgCharts['G'],
    orgCharts['H'],
    orgCharts['I'],
])
orgCharts['C'].addDirectReports([
    orgCharts['J'],
])
orgCharts['D'].addDirectReports([
    orgCharts['K'],
    orgCharts['L'],
])
orgCharts['F'].addDirectReports([
    orgCharts['M'],
    orgCharts['N'],
])
orgCharts['H'].addDirectReports([
    orgCharts['O'],
    orgCharts['P'],
    orgCharts['Q'],
    orgCharts['R'],
])
orgCharts['K'].addDirectReports([
    orgCharts['S'],
])
orgCharts['P'].addDirectReports([
    orgCharts['T'],
    orgCharts['U'],
])
orgCharts['R'].addDirectReports([
    orgCharts['V'],
])
orgCharts['V'].addDirectReports([
    orgCharts['W'],
    orgCharts['X'],
    orgCharts['Y'],
])
orgCharts['X'].addDirectReports([
    orgCharts['Z'],
])


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.helper("A", "B", "A")

    def test_case_2(self):
        self.helper("B", "F", "A")

    def test_case_3(self):
        self.helper("G", "M", "A")

    def test_case_4(self):
        self.helper("U", "S", "A")

    def test_case_5(self):
        self.helper("Z", "M", "A")

    def test_case_6(self):
        self.helper("O", "I", "B")

    def test_case_7(self):
        self.helper("T", "Z", "H")

    def test_case_8(self):
        self.helper("T", "V", "H")

    def test_case_9(self):
        self.helper("T", "H", "H")

    def test_case_10(self):
        self.helper("W", "V", "V")

    def test_case_11(self):
        self.helper("Z", "B", "B")

    def test_case_12(self):
        self.helper("Q", "W", "H")

    def test_case_13(self):
        self.helper("A", "Z", "A")

    def helper(self, a, b, c):
        lcm = program.getLowestCommonManager(orgCharts["A"], orgCharts[a], orgCharts[b])
        self.assertTrue(lcm == orgCharts[c])


if __name__ == "__main__":
	unittest.main()
