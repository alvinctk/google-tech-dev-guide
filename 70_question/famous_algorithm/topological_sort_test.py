import topological_sort as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_2(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(order, [])

    def test_case_3(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6], [4, 6], [6, 2], [2, 3]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(order, [])

    def test_case_4(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(order, [])

    def test_case_5(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        deps = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 6], [7, 8], [8, 1]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_6(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [[1, 2], [3, 5], [4, 6], [3, 6], [1, 7], [7, 8], [1, 8], [2, 8]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_7(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [
            [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
            [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8],
        ]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_8(self):
        jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        deps = [
            [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
            [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8],
            [2, 3], [2, 4], [5, 4], [7, 6], [6, 2], [6, 3],
            [6, 5], [5, 9], [9, 8], [8, 0], [4, 0], [5, 0],
            [9, 0], [2, 0], [3, 9], [3, 10], [10, 11], [11, 12], [2, 12],
        ]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_9(self):
        jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        deps = [
            [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
            [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8],
            [2, 3], [2, 4], [5, 4], [7, 6], [6, 2], [6, 3],
            [6, 5], [5, 9], [9, 8], [8, 0], [4, 0], [5, 0],
            [9, 0], [2, 0], [3, 9], [3, 10], [10, 11], [11, 12], [12, 2],
        ]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(order, [])

    def test_case_10(self):
        jobs = [1, 2, 3, 4]
        deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_11(self):
        jobs = [1, 2, 3, 4, 5]
        deps = []
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_12(self):
        jobs = [1, 2, 3, 4, 5]
        deps = [[1, 4], [5, 2]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)


def isValidTopologicalOrder(order, jobs, deps):
    visited = {}
    for candidate in order:
        for prereq, job in deps:
            if candidate == prereq and job in visited:
                return False
        visited[candidate] = True
    for job in jobs:
        if job not in visited:
            return False
    return len(order) == len(jobs)


if __name__ == "__main__":
	unittest.main()
