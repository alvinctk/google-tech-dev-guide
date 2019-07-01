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


def getLowestCommonManager(topManager, reportOne, reportTwo, debug=None):
    getLowestCommonManager_1(topManager, reportOne, reportTwo, debug=True)
    return getLowestCommonManager_2(topManager, reportOne, reportTwo, debug=True)


def getLowestCommonManager_2(topManager, reportOne, reportTwo, debug=None):
    lcm = None
    if reportOne is topManager or reportTwo is topManager:
        print_result(topManager.name, reportOne.name, reportTwo.name, topManager)
        lcm = topManager
    else:
        lcm, fx, fy = get_org(topManager, reportOne, reportTwo,None, False, False, debug)
        if debug: print("lcm2", lcm.name if lcm else None, fx, fy)
    print_result(topManager.name, reportOne.name, reportTwo.name, lcm.name if lcm else None)
    return lcm

def get_org(manager, x, y, lcm, found_x, found_y, debug=None):
    found_x = found_x | (x in manager.directReports)
    found_y = found_y | (y in manager.directReports)
    if found_x and found_y:
        return lcm, found_x, found_y

    if x in manager.directReports:
        print("found x", x.name, found_x, found_y)

    if y in manager.directReports:
        print("found y", y.name, found_x, found_y)

    for employee in manager.directReports:
        print("visit ", manager.name, employee.name, found_x, found_y)
        lcm, temp_found_x, temp_found_y = get_org(employee, x, y, lcm, found_x, found_y)
        print ("manager", manager.name, "emp", employee.name, "lcm", lcm.name if lcm else None, "f", temp_found_x, temp_found_y)
        if lcm:
            print("back track up found", found_x, found_y, manager.name, employee.name)
            return lcm, found_x, found_y

        found_x |= temp_found_x
        found_y |= temp_found_y

        if not lcm and found_x and found_y:
            print("found 3", found_x, found_y, manager.name, employee.name)
            lcm = employee
            return lcm, found_x, found_y
        else:
            print("not found", found_x, found_y, manager.name, employee.name)

    print("return outside",manager.name if manager else None, x.name, y.name, lcm, found_x, found_y)
    return lcm, found_x, found_y


def getLowestCommonManager_1(topManager, reportOne, reportTwo, debug=True):
    """
    Using extra variable depth and stack trace to find lcm.
    """
    if reportOne is topManager or reportTwo is topManager:
        print_result(topManager.name, reportOne.name, reportTwo.name, topManager)
        return topManager

    one_found, one_depth, one_trace = get_depth(topManager, reportOne, 0, [])
    two_found, two_depth, two_trace = get_depth(topManager, reportTwo, 0, [])

    if debug:
        print(topManager.name, reportOne.name, reportTwo.name)
        print("Report one manager trace", [x.name for x in one_trace])
        print("Report two manager trace", [x.name for x in two_trace])

    if one_found and two_found:
        d = abs(one_depth - two_depth)
        lower, higher = (one_trace, two_trace) if one_depth > two_depth else (two_trace, one_trace)
        while d and lower:
            lower.pop()
            d -= 1
        while lower and higher and lower[-1] is not higher[-1]:
            lower.pop()
            higher.pop()

        print_result(topManager.name, reportOne.name, reportTwo.name, lower[-1].name)
        return lower[-1]

    else:
        return None

def get_depth(manager, report, depth, trace):
    trace.append(manager)
    if report in manager.directReports:
        trace.append(report)
        return True, depth+1, trace

    for employee in manager.directReports:
        found, report_depth, trace = get_depth(employee, report, depth+1, trace)
        if found:
            return found, report_depth, trace
    trace.pop()
    return False, -1, trace

def print_result(manager, one, two, lcm):
    print("lowestCommonManager({}, {}, {}) = {}".format(manager, one, two, lcm))
    print()

if __name__ == "__main__":
    getLowestCommonManager(orgCharts['A'], orgCharts['V'], orgCharts['W'])
    getLowestCommonManager(orgCharts['A'], orgCharts['T'], orgCharts['H'])
    print()
    getLowestCommonManager(orgCharts['A'], orgCharts['Z'], orgCharts['M'])
    print()
"""
    getLowestCommonManager(orgCharts['A'], orgCharts['W'], orgCharts['V'])
    print()
    getLowestCommonManager(orgCharts['A'], orgCharts['Z'], orgCharts['B'])
    print()


    getLowestCommonManager(orgCharts['A'], orgCharts['Z'], orgCharts['M'])
    print()
    getLowestCommonManager(orgCharts['A'], orgCharts['T'], orgCharts['H'])
    print()
    getLowestCommonManager(orgCharts['A'], orgCharts['W'], orgCharts['V'])
    print()
    getLowestCommonManager(orgCharts['A'], orgCharts['Z'], orgCharts['B'])
    """

