from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        There is no rows with duplicates
        There is no columns with duplicates
        There is no sub-boxes with duplicates
        """

        # initial data
        dimension = 9
        empty = "."
        rows = [set() for i in range(dimension)]
        columns = [set() for i in range(dimension)]
        boxes = [set() for i in range(dimension)]

        for row in range(dimension):
            for col in range(dimension):
                num = board[row][col]
                if num != empty:
                    box_index = (row//3) * 3 + col//3
                    if num not in rows[row] and num not in columns[col] and num not in boxes[box_index]:
                        rows[row].add(num)
                        columns[col].add(num)
                        boxes[box_index].add(num)
                    else:
                        return False
        return True
