from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s:str, t: str) -> str:
        n, m = len(s), len(t)
        if (s == "" and t == "") or m > n:
            print("minWindow({}, {}) = \"{}\"".format(s, t, ""))
            return ""
        left = right = min_left = min_right = 0
        count = Counter(t)
        window = defaultdict(int)
        w = 0
        length = float("inf")
        while right < n:
            if w == 0 and s[right] not in count:
                left += 1
                right += 1
                continue
            if w < m and s[right] in count:
                window[s[right]] += 1
                if window[s[right]] <= count[s[right]]:
                    w += 1

            if w == m:
                #print(s[left:right+1], right - left + 1)
                if right - left + 1 < length:
                    length = right - left + 1
                    min_left = left
                    min_right = right
                if s[left] in count:
                    window[s[left]] -= 1
                    if window[s[left]] + 1 <= count[s[left]]:
                        w -= 1
                        right += 1

                left += 1
            else:
                right += 1
        result =  "" if length == float("inf") else s[min_left:min_right+1]
        print("minWindow({}, {}) = {}".format(s, t, result))
        return result

if __name__ == "__main__":
    x = Solution()
    tt = [("acbbaca", "aba")]
    #ll = [("acbbaca", "aba"), ("a", "aa"), ("ab", "b"), ("aa", "aa"), ("bba", "ba"), ("ADOBECODEBANC", "ABC"), ("ueeouptjcosytyujjcvnmtndauseqxvkdzayrtjvhdtcbnnmrjbfeokfkdjacgnhfnhwjqtsumvvckkvtlbaclfmqqpuwecdtjccavxwiutmedhapkarwhfozwlxapauyeyaavwkpswwvdwmqydoflcejpbkedgdieficeutwqrtvnglllzswewgtzsadydlekvgqpcmhtgejmqwxrpwxletnwtquybakyjbnlnuevynjqmjkbfjojcbhxrdvudismjhxybeuctdsfoegtoxesylqsonouvhgeqgdsmzwfeontvvojstbtgrlxhzrcixjzfmtrnpzrfomalbjeunzcemzllqqwqzxxnqpahqtmggprhyxdlwfsiffwxvspwrnjheloufccnrtusrzfpexalfwjcqyzhnkqrygnfipsclmuclbtrztdgroihojqcwgvumjzxarblfxpsyjjxeofwcqftzwvvesrrbsqcjrpqofimqsmuitsljyejubgytarxsjbecqusxdhnxvifoasyayjwbrxvtoumaxsenmxlrgaqbiyrlqrlraksuhppxjdxgvcwibjbhjukusbfitsbveupljhjvkgdgkzqnirwulgofivqbprwulofvvoshxvnjvdzfxvzkcnqmkgnazlulbbiyqagpvvaszzyyvxkxncjxkyzklvvnxfnpfvearetsgtsbscafflfrlgbwcylzdboiwulnagfgzxhrcjzjugafmceocrpgsdqpzbcahkggjoalzzuuhxbtzfkdxzjpdagcdlenxltgbvuawqwdnyxofhsegdulfcqjnuwkhrtinnljdhptfmhlvbpdflpkqhtddrqljjtywejb", "oyutmeghfylklcvbjqfmkxx")]
    for s, t in tt:
        x.minWindow(s, t)
