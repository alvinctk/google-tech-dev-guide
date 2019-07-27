import unittest
import minimum_substring_window as program
class TestProgram(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestProgram, self).__init__(*args, **kwargs)
        self.minWindow = program.Solution().minWindow

    def t(self, x, y, z):
        self.assertEqual(self.minWindow(x, y), z)

    def test_case1(self):
        self.t("a", "aa", "")

    def test_case2(self):
        self.t("ab", "b", "b")

    def test_case3(self):
        self.t("aa", "aa", "aa")

    def test_case4(self):
        self.t("bba", "ba", "ba")

    def test_case5(self):
        self.t("ADOBECODEBANC", "ABC", "BANC")

    def test_case6(self):
        self.t("ueeouptjcosytyujjcvnmtndauseqxvkdzayrtjvhdtcbnnmrjbfeokfkdjacgnhfnhwjqtsumvvckkvtlbaclfmqqpuwecdtjccavxwiutmedhapkarwhfozwlxapauyeyaavwkpswwvdwmqydoflcejpbkedgdieficeutwqrtvnglllzswewgtzsadydlekvgqpcmhtgejmqwxrpwxletnwtquybakyjbnlnuevynjqmjkbfjojcbhxrdvudismjhxybeuctdsfoegtoxesylqsonouvhgeqgdsmzwfeontvvojstbtgrlxhzrcixjzfmtrnpzrfomalbjeunzcemzllqqwqzxxnqpahqtmggprhyxdlwfsiffwxvspwrnjheloufccnrtusrzfpexalfwjcqyzhnkqrygnfipsclmuclbtrztdgroihojqcwgvumjzxarblfxpsyjjxeofwcqftzwvvesrrbsqcjrpqofimqsmuitsljyejubgytarxsjbecqusxdhnxvifoasyayjwbrxvtoumaxsenmxlrgaqbiyrlqrlraksuhppxjdxgvcwibjbhjukusbfitsbveupljhjvkgdgkzqnirwulgofivqbprwulofvvoshxvnjvdzfxvzkcnqmkgnazlulbbiyqagpvvaszzyyvxkxncjxkyzklvvnxfnpfvearetsgtsbscafflfrlgbwcylzdboiwulnagfgzxhrcjzjugafmceocrpgsdqpzbcahkggjoalzzuuhxbtzfkdxzjpdagcdlenxltgbvuawqwdnyxofhsegdulfcqjnuwkhrtinnljdhptfmhlvbpdflpkqhtddrqljjtywejb"
, "oyutmeghfylklcvbjqfmkxx", "kyjbnlnuevynjqmjkbfjojcbhxrdvudismjhxybeuctdsfoegtoxesyl")

if __name__ == "__main__":
    unittest.main()
