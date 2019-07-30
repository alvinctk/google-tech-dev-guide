from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        def explore(i,j):

            # i was here
            grid[i][j] = 'x'

            if i > 0 and grid[i - 1][j] == '1':
                explore(i - 1,j)

            if j > 0 and grid[i][j - 1] == '1':
                explore(i,j - 1)

            if i < col - 1 and grid[i + 1][j] == '1':
                explore(i + 1,j)

            if j < row - 1 and grid[i][j + 1] == '1':
                explore(i,j + 1)

        islands = 0

        col = len(grid)
        row = len(grid[0])

        for i in range(col):
            for j in range(row):

                if grid[i][j] == '1':

                    islands += 1

                    # Mark all the points in this island i.e all the points that can be reached from this point
                    explore(i,j)


        return islands
    def xnumIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n >= 1 else 0
        if m == 0 or n == 0:
            return 0
        grid = [[1 if x == "1" else 0 for x in row] for row in grid]
        visited = [[False] * m for _ in range(n)]
        islands = 0

        for i in range(n):
            for j in range(m):
                print("grid[{i}][{j}] = {} and not visited[{i}][{j}]={}".format(grid[i][j], not visited[i][j], i=i, j=j))
                if grid[i][j] and not visited[i][j]:
                    islands += 1
                    self.visit_island(i, j, grid, visited)
                    print(islands)
                    g = 0
                    while g < n:
                        print(grid[g])
                        print(visited[g])
                        print()
                        g += 1
        return islands

    def visit_island(self, i: int, j: int, grid: List[List[int]], visited: List[List[bool]]):
        q = deque()
        q.append((i, j))
        while q:
            print(q, len(q))
            x, y = q.popleft()
            visited[x][y] = True
            self.add_island(q, x, y, grid, visited)

    def add_island(self, q: deque, i: int, j: int, grid: List[List[int]], visited: List[List[bool]]):
        # up
        if i - 1 >= 0 and grid[i-1][j] and not visited[i-1][j]:
            q.append((i-1, j))
        # down
        if i + 1 < len(grid) and grid[i+1][j] and not visited[i+1][j]:
            q.append((i+1, j))
        # right
        if j + 1 < len(grid[0]) and grid[i][j+1] and not visited[i][j+1]:
            q.append((i, j+1))
        # left
        if j - 1 >= 0 and grid[i][j-1] and not visited[i][j-1]:
            q.append((i, j-1))

if __name__ == "__main__":
    x = Solution()
    grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
            ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
            ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
            ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
            ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]


    #grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(x.numIslands(grid))

