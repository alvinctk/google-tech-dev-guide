"""
Suffix Trie Construction
"""

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_trie(string)

    def populate_suffix_trie(self, string):
        for i, _ in enumerate(string):
            self.insert_suffix(string, i)

    def insert_suffix(self, string, start):
        current = self.root
        for letter in string[start:]:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def contains(self, string):
        current = self.root
        for c in string:
            if c not in current:
                return False
            current = current[c]
        return self.end_symbol in current





