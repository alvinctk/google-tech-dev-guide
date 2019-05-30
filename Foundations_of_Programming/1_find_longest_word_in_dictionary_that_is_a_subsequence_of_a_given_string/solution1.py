
"""
set n to length of s
set m to length of w

set i to first index of s
set j to first index of w

while i is less than n
     if s[i] is equal to w[j], then increment i and j by 1
     if s[i] is not equal to w[j], then increment i by 1
return m == j (True if all w in s matches, otherwise False.)
"""

def is_subsequence(s, w, debug=False):
    """
    s is string S
    w is word W in dictionary
    Returns True if w is subsequence in S. Otherwise, False.
    """

    n, m = len(s), len(w)
    i, j = 0, 0
    k = 0

    sufficient_len = lambda i, j: (n - i) - (m - j) >= 0
    # Greedy algorithm, search at each index of S
    while i < n and j < m and sufficient_len(i, j):
        # base case when subsequence is found
        if j == m:
            break
        if s[i] == w[j]:
            # alphabet at index i,j matches
            i += 1
            j += 1
        else:
            # does not match at index i,j
            i += 1
        if debug:
            print("k = {}, i = {}, j = {}, s = {}, w = {}".format(k , i, j, s[i:], w[j:]))
        k += 1

    if debug: print("m = ", j, m)
    return j == m

def find_longest_word(s, d, debug=False, result=True):

    # Find all word that are subsequence of S
    x = [word for word in d if is_subsequence(s,word, debug)]

    if result: print("String S = {}".format(s))
    if result: print("Subsequence in S = {}".format(x))
    if result: print("Dictionary in D = {}".format(d))

    # Find the longest word in the result list
    longest_word =  max(x, key=len) if x else None

    if result: print("Longest subsequence word in d = {}".format(longest_word))

    return longest_word
if __name__ == "__main__":
    s1 = "abpcplea"
    d1 = {"ale", "apple", "monkey", "plea"}
    r1 = "apple"

    s0 = "abppplee"
    d0 = {"able", "ale", "apple", "bale", "kangaroo"}
    r0 = "apple"

    d2 = {"pintu", "geeksfor", "geeksgeeks", " forgeek"}
    s2 = "geeksforgeeks"
    r2 = "geeksgeeks"

    for s, d, r in [(s0, d0, r0),(s1, d1, r1),(s2, d2, r2)]:
        find_longest_word(s, d, debug=False)
        print()
        #assert find_longest_word(s, d) == r, "Should be {}".format(r)
