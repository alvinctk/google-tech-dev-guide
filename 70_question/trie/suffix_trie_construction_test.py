import suffix_trie_construction as program
import unittest


word1 = "test"
test1 = program.SuffixTrie(word1)
trie1 = {
    "t": {
        "*": True,
        "e": {"s": {"t": {"*": True}}},
    },
    "s": {"t": {"*": True}},
    "e": {"s": {"t": {"*": True}}},
}

word2 = "invisible"
test2 = program.SuffixTrie(word2)
trie2 = {
    "e": {"*": True},
    "l": {"e": {"*": True}},
    "b": {"l": {"e": {"*": True}}},
    "i": {
        "b": {"l": {"e": {"*": True}}},
        "s": {"i": {"b": {"l": {"e": {"*": True}}}}},
        "n": {"v": {"i": {"s": {"i": {"b": {"l": {"e": {"*": True}}}}}}}},
    },
    "s": {"i": {"b": {"l": {"e": {"*": True}}}}},
    "v": {"i": {"s": {"i": {"b": {"l": {"e": {"*": True}}}}}}},
    "n": {"v": {"i": {"s": {"i": {"b": {"l": {"e": {"*": True}}}}}}}},
}

word3 = "1234556789"
test3 = program.SuffixTrie(word3)
trie3 = {
    "9": {"*": True},
    "8": {"9": {"*": True}},
    "7": {"8": {"9": {"*": True}}},
    "6": {"7": {"8": {"9": {"*": True}}}},
    "5": {
        "6": {"7": {"8": {"9": {"*": True}}}},
        "5": {"6": {"7": {"8": {"9": {"*": True}}}}},
    },
    "4": {"5": {"5": {"6": {"7": {"8": {"9": {"*": True}}}}}}},
    "3": {"4": {"5": {"5": {"6": {"7": {"8": {"9": {"*": True}}}}}}}},
    "2": {"3": {"4": {"5": {"5": {"6": {"7": {"8": {"9": {"*": True}}}}}}}}},
    "1": {"2": {"3": {"4": {"5": {"5": {"6": {"7": {"8": {"9": {"*": True}}}}}}}}}},
}

word4 = "testtest"
test4 = program.SuffixTrie(word4)
trie4 = {
    "e": {"s": {"t": {
        "*": True,
        "t": {"e": {"s": {"t": {"*": True}}}}}}
    },
    "t": {
        "*": True,
        "e": {"s": {"t": {
            "*": True,
            "t": {"e": {"s": {"t": {"*": True}}}}}},
        },
        "t": {"e": {"s": {"t": {"*": True}}}},
    },
    "s": {"t": {
        "*": True,
        "t": {"e": {"s": {"t": {"*": True}}}}}
    },
}

word5 = "ttttttttt"
test5 = program.SuffixTrie(word5)
trie5 = {
    "t": {
        "*": True,
        "t": {
            "*": True,
            "t": {
                "*": True,
                "t": {
                    "*": True,
                    "t": {
                        "*": True,
                        "t": {
                            "*": True,
                            "t": {
                                "*": True,
                                "t": {
                                    "*": True,
                                    "t": {"*": True}}}}}}}}},
}

word6 = "babc"
test6 = program.SuffixTrie(word6)
trie6 = {
    "c": {"*": True},
    "b": {
        "c": {"*": True},
        "a": {"b": {"c": {"*": True}}},
    },
    "a": {"b": {"c": {"*": True}}},
}


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        for i in reversed(range(len(word1))):
            substring = word1[i:]
            self.assertEqual(test1.contains(substring), True)

    def test_case_2(self):
        for i in reversed(range(len(word2))):
            substring = word2[i:]
            self.assertEqual(test2.contains(substring), True)

    def test_case_3(self):
        for i in reversed(range(len(word3))):
            substring = word3[i:]
            self.assertEqual(test3.contains(substring), True)

    def test_case_4(self):
        for i in reversed(range(len(word4))):
            substring = word4[i:]
            self.assertEqual(test4.contains(substring), True)

    def test_case_5(self):
        for i in reversed(range(len(word5))):
            substring = word5[i:]
            self.assertEqual(test5.contains(substring), True)

    def test_case_6(self):
        for i in reversed(range(len(word6))):
            substring = word6[i:]
            self.assertEqual(test6.contains(substring), True)

    def test_case_7(self):
        self.assertEqual(test1.root, trie1)

    def test_case_8(self):
        self.assertEqual(test2.root, trie2)

    def test_case_9(self):
        self.assertEqual(test3.root, trie3)

    def test_case_10(self):
        self.assertEqual(test4.root, trie4)

    def test_case_11(self):
        self.assertEqual(test5.root, trie5)

    def test_case_12(self):
        self.assertEqual(test6.root, trie6)

    def test_case_13(self):
        self.assertEqual(test1.contains("tes"), False)

    def test_case_14(self):
        self.assertEqual(test2.contains("nvisibl"), False)

    def test_case_15(self):
        self.assertEqual(test3.contains("45567"), False)

    def test_case_16(self):
        self.assertEqual(test4.contains("tt"), False)

    def test_case_17(self):
        self.assertEqual(test5.contains("vvv"), False)

    def test_case_18(self):
        self.assertEqual(test6.contains("bab"), False)


if __name__ == "__main__":
	unittest.main()
