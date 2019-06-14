import caesar_cipher as program
import unittest

class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(program.caesar_cipher_encryptor("abc", 0), "abc")

    def test_case_2(self):
        self.assertEqual(program.caesar_cipher_encryptor("abc", 3), "def")

    def test_case_3(self):
        self.assertEqual(program.caesar_cipher_encryptor("xyz", 2), "zab")

    def test_case_4(self):
        self.assertEqual(program.caesar_cipher_encryptor("xyz", 5), "cde")

    def test_case_5(self):
        self.assertEqual(program.caesar_cipher_encryptor("abc", 26), "abc")

    def test_case_6(self):
        self.assertEqual(program.caesar_cipher_encryptor("abc", 52), "abc")

    def test_case_7(self):
        self.assertEqual(program.caesar_cipher_encryptor("abc", 57), "fgh")

if __name__ == "__main__":
    unittest.main()

