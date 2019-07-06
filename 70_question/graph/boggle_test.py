import boggle as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        board = [
            ["y", "g", "f", "y", "e", "i"],
            ["c", "o", "r", "p", "o", "u"],
            ["j", "u", "z", "s", "e", "l"],
            ["s", "y", "u", "r", "h", "p"],
            ["e", "a", "e", "g", "n", "d"],
            ["h", "e", "l", "s", "a", "t"],
        ]
        words = ["san", "sana", "at", "vomit", "yours", "help", "end", "been", "bed", "danger", "calm", "ok", "chaos", "complete", "rear", "going", "storm", "face", "epual", "dangerous"]
        expected = ["yours", "help", "danger", "san", "at"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_2(self):
        board = [
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "j"],
            ["k", "l", "m", "n", "o"],
            ["p", "q", "r", "s", "t"],
            ["u", "v", "w", "x", "y"],
        ]
        words = ["agmsy", "agmsytojed", "agmsytojedinhcbgl", "agmsytojedinhcbfl"]
        expected = ["agmsy", "agmsytojed", "agmsytojedinhcbfl"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_3(self):
        board = [
            ["a", "b"],
            ["c", "d"],
        ]
        words = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "abca"]
        expected = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_4(self):
        board = [
            ["f", "t", "r", "o", "p", "i", "k", "b", "o"],
            ["r", "w", "l", "p", "e", "u", "e", "a", "b"],
            ["j", "o", "t", "s", "e", "l", "f", "l", "p"],
            ["s", "z", "u", "t", "h", "u", "o", "p", "i"],
            ["k", "a", "e", "g", "n", "d", "r", "g", "a"],
            ["h", "n", "l", "s", "a", "t", "e", "t", "x"],
        ]
        words = ["frozen", "rotten", "teleport", "city", "zutgatz", "kappa", "before", "rope", "obligate", "annoying"]
        expected = ["frozen", "rotten", "teleport", "kappa", "before", "rope", "obligate"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_5(self):
        board = [
            ["c", "o", "m"],
            ["r", "p", "l"],
            ["c", "i", "t"],
            ["o", "a", "e"],
            ["f", "o", "d"],
            ["z", "r", "b"],
            ["g", "i", "a"],
            ["o", "a", "g"],
            ["f", "s", "z"],
            ["t", "e", "i"],
            ["t", "w", "d"],
        ]
        words = ["commerce", "complicated", "twisted", "zigzag", "comma", "foobar", "baz", "there"]
        expected = ["complicated", "twisted", "zigzag", "foobar"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_6(self):
        board = [
            ["c", "o", "m"],
            ["r", "p", "l"],
            ["c", "i", "t"],
            ["o", "a", "e"],
            ["f", "o", "d"],
            ["z", "r", "b"],
            ["g", "i", "a"],
            ["o", "a", "g"],
            ["f", "s", "z"],
            ["t", "e", "i"],
            ["t", "w", "d"],
        ]
        words = ["cr", "oc", "ml", "iao", "opo", "zrb", "big", "fs", "ogiagao", "dwd", "twt"]
        expected = ["cr", "oc", "ml", "iao", "zrb", "big", "fs", "twt"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_7(self):
        board = [
            ["c", "o", "m"],
            ["r", "p", "l"],
            ["c", "i", "t"],
            ["o", "a", "e"],
            ["f", "o", "d"],
            ["z", "r", "b"],
            ["g", "i", "a"],
            ["o", "a", "g"],
            ["f", "s", "z"],
            ["t", "e", "i"],
            ["t", "w", "d"],
        ]
        words = ["comlpriteacoofziraagsizefttw", "comlpriteacoofzirabagsizefottw", "comlpriteacoofziraagsizefottw", "comlpriteacoofzirabagsizeftttw"]
        expected = ["comlpriteacoofziraagsizefttw"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_8(self):
        board = [
            ["t", "h", "i", "s", "i", "s", "a"],
            ["s", "i", "m", "p", "l", "e", "x"],
            ["b", "x", "x", "x", "x", "e", "b"],
            ["x", "o", "g", "g", "l", "x", "o"],
            ["x", "x", "x", "D", "T", "r", "a"],
            ["R", "E", "P", "E", "A", "d", "x"],
            ["x", "x", "x", "x", "x", "x", "x"],
            ["N", "O", "T", "R", "E", "-", "P"],
            ["x", "x", "D", "E", "T", "A", "E"],
        ]
        words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
        expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
        actual = program.boggleBoard(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)


if __name__ == "__main__":
	unittest.main()
