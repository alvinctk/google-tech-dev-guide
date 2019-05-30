"""
while i is less than n
     let l be the list of index in s for character at w[j], where l = y[w[j]]
     find index t of w[j] in s such that min(t >= i in l)
     if t is found, then set i to t+1 and increment j by 1
     else t is not found, then increment i by 1
Return j==m (True if j==m, since all of letters of w is found,
             False if j!=m, since at least one letters of w is not found

Worse case: A word W that has no matches in S
To optimize: To avoid checking every index of S, we can stop when there is insufficient characters in S to form word W. Time complexity for optimization worse case is O(1). The algorithm is as follows:
Suppose i is the character index of String S to be matched against word W.
Suppose j is the character index of word W.
Suppose n is the length of S and m is the length of W.
For word W to be a subsequence of string S,
there must be at least (n - i - 1) - (m - j - 1) >= 0 characters left.
The equation can be simplified to n - i - (m - j) > 0
Note that if n = m, then n- i - (m-j) must be zero.
"""

from collections import defaultdict

def preprocess_s(s):
    """
    s = string S

    Preprocess the string s into a map such that
    key = a unique character of S
    value = list of ordered index for character occurs in S
    """
    y = defaultdict(list)
    for i, c in enumerate(s):
        y[c].append(i)
    return y

def is_subsequence2(s, w, y, debug=True):
    """
    s = string S
    w = word W to test if W is a subsequence in S
    y = preprocess dictionary of list of index for a particular character

    Return True if w is a subsequence. Otherwise, False

    Example:
    s = "abppplee"
    w = "apple"
    y = defaultdict(<class 'list'>, {'a': [0], 'b': [1], 'p': [2, 3, 4], 'l': [5], 'e': [6, 7]})
    is_subsequence(s, w, y) returns True since "apple" is a substring
    """
    n, m = len(s), len(w)
    i, j = 0, 0
    e = 0
    sufficient_len = lambda i, j: (n - i) - (m - j) >= 0
    while i < n and j < m and sufficient_len(i, j):

        if debug: print("j={}, w[j] = {}".format(j, w[j]))

        # l is the list of index in s for character at w[j]

        l = y[w[j]] if w[j] in y else None
        if debug: print("l={}, w[j]={}, j={}".format(l, w[j], j))

        # Find index t of w[j] in s such that min(t >= i in l)
        q = [k for k in l if k >= i] if l else None
        t = min(q) if q else None
        #t = min(k for k in l if k >= i) if l else None

        # Use t is not None to compare since possible t values are 0.
        if t is not None:
            # The letter of a word w in a dictionary D is found at index t of string S
            i = t+1
            j += 1
            if debug: print("k = {}, i = {}, j = {}, q = {}, t = {}, s = {}, w = {}"
                            .format(e, i, j, q, t, s[i:], w[j:]))
        else:
            # The letter of a word w is not found in string S
            i += 1
            if debug: print("k = {}, i = {}, j = {}, s = {}, w = {}".format(k , i, j, s[i:], w[j:]))
        if debug: print()

        # For debug purpose to count number of loops
        if debug: e += 1

    # Returns True if all letters of word w is found in string S. Otherwise, False
    return j == m

def find_longest_word2(s, d, y, r=None, debug=False, result=True):
    """
    s = string S
    d = dictionary of word W
    y = preprocess dictioanry of list of index for a unique character in string S
    r = result to assert find_longest_word2
    """
    if result: print("String S = {}".format(s))
    if result: print("Dictionary D = {}".format(d))

    # Compute all word in dictionary if the word is a subsequence of S and store in a list x
    x = [word for word in d if is_subsequence2(s, word, y, debug=debug)]
    if result: print("subsequence in S = {}".format(x))

    # Find the longest word in the result list
    longest_word =  max(x, key=len) if x else None
    if result: print("Longest subsequence word in d = {}".format(longest_word))
    assert longest_word == r, "Should be {}".format(r)
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

    for s, d, r in [(s0, d0, r0), (s1, d1, r1),(s2, d2, r2)]:

        find_longest_word2(s, d, preprocess_s(s), r)
        print()
