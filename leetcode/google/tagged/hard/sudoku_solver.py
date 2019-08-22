from typing import List
from collections import defaultdict

class Sudoku:
    def __init__(self, board):

        self.board = board
        self.DIMENSION = 9
        self.MAX_SQUARES = self.DIMENSION ** 2
        self.BLOCK_PER_RC = 3

        # i-th value available represent by 1 bit from 1-th to self.DIMENSION-th
        self.ONES = 0x3fe # (0011 1111 1110) to
        self.ZEROS = 0
        self.EMPTY = "."

        self.rows = [self.ONES] * self.DIMENSION
        self.columns = [self.ONES] * self.DIMENSION
        self.blocks = [self.ONES] * self.DIMENSION
        self.address = [0] * self.MAX_SQUARES
        self.entries = [0] * self.MAX_SQUARES

        self.entry_string = defaultdict(str)
        self.search_spaces = defaultdict(int)
        self.sequences = []

        self.initialize_value_mask()
        self.initialize_each_square()
        #print("before build sequences",len(self.sequences), self.sequences)
        self.fill_one_space()
        #print("after build sequences", len(self.sequences), self.sequences)


    def initialize_value_mask(self) -> None:
        """
        Map each value mask to a value from 0 to 9.
        Helps for faster access when placing solved values onto the board.
        """
        mask, value = 2, 1
        while mask <= self.ONES:
            self.entry_string[mask] = str(value)
            value += 1
            mask <<= 1

    def initialize_each_square(self) -> None:
        """
        Initialize each square's block, row, col 's bitmap
        Append squares that are empty to the sequences
        """
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):

                square = self.DIMENSION * row + col
                block = (row//self.BLOCK_PER_RC) * 3 + (col//self.BLOCK_PER_RC)
                self.address[square] = (block, row, col)

                if self.board[row][col] != self.EMPTY:
                    value = int(self.board[row][col])
                    value_mask = 1 << value
                    self.set_value_unavailable(square, value_mask)
                else:
                    self.sequences.append(square)

    def build_sequences(self, sequences: List[int]) -> List[int]:
        """
        Build sequences by solving the square that only has one value
        Return sorted sequences with the least search space in front
        """
        if not sequences:
            return sequences
        ones = []
        others = []
        for square in sequences:
            possible = self.possible_values(square)
            search_space = self.count_available_bits(square)

            if search_space == 1:
                block, row, col = self.address[square]
                self.board[row][col] = self.entry_string[possible]
                #self.entries[square] = possible
                self.set_value_unavailable(square, possible)
            else:
                others.append(square)
                self.search_spaces[square] = search_space
        others.sort(key=lambda square: self.search_spaces[square])
        return others

    def fill_one_space(self) -> None:
        """
        Keeps filling the one space squares until no more one search space left
        """
        self.sequences = self.build_sequences(self.sequences)
        while self.sequences and self.count_available_bits(self.sequences[0]) == 1:
            self.sequences = self.build_sequences(self.sequences)

    def count_available_bits(self, square: int) -> int:
        """
        Count the square's availability bitmask = total possible values at square
        """
        possible = self.possible_values(square)
        count = 0
        while possible:
            #print("count bits: square={} possible={} count{}".format(square, bin(possible), count))
            # Set the rightmost 1-bit to 0
            possible &= ~(possible & -possible)
            count += 1
        return count

    def next_seq(self, position: int) -> int:
        """
        Retrieve the next square position with the least possible values
        """
        min_space = 100
        min_seq = position
        for seq in range(position, len(self.sequences)):
            square = self.sequences[seq]
            search_space = self.count_available_bits(square)
            if search_space < min_space:
                min_space = search_space
                min_seq = seq
        return min_seq

    def possible_values(self, square: int) -> int:
        """
        Return the square's bitmask of possible values
        """
        block, row, col = self.address[square]
        return self.blocks[block] & self.rows[row] & self.columns[col]

    def set_value_available(self, square: int, mask: int) -> None:
        """
        Helper to set value to available for all of square's bitmask
        """
        block, row, col = self.address[square]
        self.blocks[block] |= mask
        self.rows[row] |= mask
        self.columns[col] |= mask

    def set_value_unavailable(self, square: int, mask: int) -> None:
        """
        Helper to set value to be unavailable for all of square's bitmask
        """
        block, row, col = self.address[square]
        self.blocks[block] &= ~mask
        self.rows[row] &= ~mask
        self.columns[col] &= ~mask

    def swap_sequences(self, a: int, b: int) -> None:
        """
        Helper to swap square values at two sequences indexes
        """
        self.sequences[a], self.sequences[b] = self.sequences[b], self.sequences[a]

    def place(self, seq: int) -> bool:
        """
        Main function to place each value at a square.
        place will try the square with the least possible values
        """
        if seq == len(self.sequences):
            return True

        next_seq = self.next_seq(seq)
        self.swap_sequences(seq, next_seq)

        square = self.sequences[seq]
        possible = self.possible_values(square)
        #print("place, square={} seq={}".format(square, seq))
        while possible:
            # Get the rightmost bit
            value_mask = possible & -possible
            # Set the rightmost bit to 0
            possible &= ~value_mask
            self.set_value_unavailable(square, value_mask)
            self.entries[square] = value_mask

            if self.place(seq+1):
                return True

            # Rest the square bitmask
            self.set_value_available(square, value_mask)

        # Reset the swap of squares
        self.swap_sequences(seq, next_seq)

        return False

    def place_solved_values(self):
        """
        Place the solved values onto the sudoku board
        """
        for square in self.sequences:
            block, row, col = self.address[square]
            self.board[row][col] = self.entry_string[self.entries[square]]

    def print_board(self):
        """
        Helper to print sudoku board
        """
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                print(self.board[row][col], end=" ")
            print()

    def solve_board(self):
        """
        Main solve function for sudoku
        """
        solve = self.place(0)
        if solve:
            print("Solved sudoku board")
            self.place_solved_values()
            self.print_board()
        else:
            print("Fail to solve sudoku board")

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything
        Time complexity: O(N log N) + O(M^2) <= O(N^2)
            O(1) times to sort after filled ones =O(1) * O(N log N)
            M = N - K, where K represent filled ones, M represent empty squares
            Traversing down the sequences = O(M ^ 2), since M times to call next_seq
            next seq = O(M)

        Space complexity: O(D) where D = dimension of a row
        Runtime: 48 ms, faster than 95.57% of Python3 online submissions for Sudoku Solver.
        Memory Usage: 13.9 MB, less than 10.71% of Python3 online submissions for Sudoku Solver.
        """
        sudoku_solver = Sudoku(board)
        sudoku_solver.solve_board()

if __name__ == "__main__":
    board  = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    s.solveSudoku(board)
