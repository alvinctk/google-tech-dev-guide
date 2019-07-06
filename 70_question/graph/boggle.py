class Boggle:
    def __init__(self, board, words):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0]) if board else 0
        self.words = words
        self.trie = Trie()
        self.visited = None
        self.final_words = None
        for word in words:
            self.trie.populate_word(word)

    def boggle_board(self):
        visited = [[False]*self.columns for _ in range(self.rows)]
        final_words = {}
        for i in range(self.rows):
            for j in range(self.columns):
                self.explore(i, j, self.trie.root, visited, final_words)
        return list(final_words.keys())

    def explore(self, i, j, trieNode, visited, final_words):
        if visited[i][j]:
            return
        letter = self.board[i][j]
        if letter not in trieNode:
            return

        visited[i][j] = True
        trieNode = trieNode[letter]

        if self.trie.end_symbol in trieNode:
            final_words[trieNode[self.trie.end_symbol]] = True

        for x, y in self.get_neighbors(i, j):
            self.explore(x, y, trieNode, visited, final_words)

        visited[i][j] = False

    def get_neighbors(self, i, j):
        neighbors = []
        # left
        if j > 0:
            neighbors.append((i, j - 1))

        # right
        if j + 1 < self.columns:
            neighbors.append((i, j + 1))
        # up
        if i > 0:
            neighbors.append((i - 1, j))

        # down
        if i + 1 < self.rows:
            neighbors.append((i + 1, j))

        # diagonal up left
        if i > 0 and j > 0:
            neighbors.append((i - 1, j - 1))
        # diagonal up right
        if i > 0 and j + 1 < self.columns:
            neighbors.append((i - 1, j + 1))
        # diagonal down left
        if i + 1 < self.rows and j > 0:
            neighbors.append((i + 1, j -1))
        # diagonal down right
        if i + 1 < self.rows and j + 1 < self.columns:
            neighbors.append((i + 1, j + 1))

        return neighbors

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def populate_word(self, string):
        current = self.root
        for letter in string:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = string

    def contains(self, string):
        current = self.root
        for c in string:
            if c not in current:
                return False
            current = current[c]
        return self.end_symbol in current

def boggleBoard(board, words):
    b = Boggle(board, words)
    return b.boggle_board()
