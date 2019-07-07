class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def populate_word(self, string, start):
        n = len(string)
        current = self.root
        while start < n and string[start] != " ":
            c = string[start]
            if c not in current:
                current[c] = {}

            current = current[c]
            start += 1

        current[self.end_symbol] = True
        return start

    def populate_words(self, string):
        n = len(string)
        start = 0
        while start < n:
            start = self.populate_word(string, start)
            start += 1

    def contains(self, string):
        current = self.root
        for c in string:
            if c in current:
                current = current[c]
            else:
                return False

        # Since the query strings does not have to be equal to end of word
        return True
    def multi_string_search(self, big_string, list_of_strings):
        self.populate_words(big_string)
        return [self.contains(string) for string in list_of_strings]

if __name__ == "__main__":
    t = Trie()

    y = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
    z = "this is a big string"
    print(z)
    print(y)
    x = t.multi_string_search(z, y)
    print(x)
