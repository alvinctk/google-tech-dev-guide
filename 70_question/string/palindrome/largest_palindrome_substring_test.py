# Add, edit, or remove tests in this file.
# Treat it as your playground!
import largest_palindrome_substring as program
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.longestPalindromicSubstring("a"), "a")

    def test_case_2(self):
        self.assertEqual(program.longestPalindromicSubstring("it's highnoon"), "noon")

    def test_case_3(self):
        self.assertEqual(program.longestPalindromicSubstring("noon high it is"), "noon")

    def test_case_4(self):
        self.assertEqual(program.longestPalindromicSubstring("abccbait's highnoon"), "abccba")

    def test_case_5(self):
        self.assertEqual(program.longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")

    def test_case_6(self):
        self.assertEqual(program.longestPalindromicSubstring("abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"), "zzzzzzzzzzzzzzzzzzzz")

    def test_case_7(self):
        self.assertEqual(program.longestPalindromicSubstring("abcdefgfedcba"), "abcdefgfedcba")

    def test_case_8(self):
        self.assertEqual(program.longestPalindromicSubstring("abcdefghfedcbaa"), "aa")

    def test_case_9(self):
        self.assertEqual(program.longestPalindromicSubstring("abcdefggfedcba"), "abcdefggfedcba")

    def test_case_10(self):
        self.assertEqual(program.longestPalindromicSubstring("zzzzzzz2345abbbba5432zzbbababa"), "zz2345abbbba5432zz")

    def test_case_11(self):
        self.assertEqual(program.longestPalindromicSubstring("z234a5abbbba54a32z"), "5abbbba5")

    def test_case_12(self):
        self.assertEqual(program.longestPalindromicSubstring("z234a5abbba54a32z"), "5abbba5")


if __name__ == "__main__":
    unittest.main()

