"""
Problem:

Given two strings, base and remove, return a version of the base string
where all instances of the remove string have been removed (not case sensitive).
You may assume that the remove string is length 1 or more.
Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"

# Set original string to be as s. Let n be length of s.
# Set string that indicates what to remove as r. Let m be length of r.
# Set string to be modified and returned as q.

# Preprocess the indices in s such that a dictionary stores for each unique
# character, there's a list of indices where character occurs. Let y be the
# preprocess list. Example for character "H", y["H"] = [0, 7].

# Using the preprocess dictionary of list of indices at each unique value of s.
# i := 0
# modified := empty string
# Iterate each indices of r[0] that occurs in s.
#     If i is less than or equal to index of r[0]
#       and there is sufficient length to remove
#       and the substring in s to remove is equal to r
#     then
#       set modified to values before removal
#       set i to index after last character of removed sequence
#
# If i is less than n, then add all of the remaining characters in s from index
# i
#
# Space complexity: O(n) to construct the preprocess indices
# Time complexity:
# Best case is O(1), since there isn't any r[0] in s.
# Worse case is O(p), where p is the number of r[0] in s, since every r[0]
# needs to be removed. p <= n.
"""

from collections import defaultdict
def withoutString(s, r):
    """
    s = string to be modify
    r = string to remove from s

    return a modified string
    """
    # Preprocess the list to store indices
    y = defaultdict(list)
    for s_i, x in enumerate(s):
        y[x].append(s_i)

        # To stop checking there isn't sufficient length for comparsion.
    sufficient_len = lambda i: n - i -m >= 0

    i = 0
    n, m = len(s), len(r)
    modified = ""

    # If y[r[0]] is empty, it will skip the for loop
    # Construct the modified string according to string s and r.
    # To optimize checking each index, we simply tranverse to all possible
    # index at which r[0] begins in string s.
    for s_r in y[r[0]]:

        # The string we want to remove is from s_r to s_r + m - 1 inclusively.
        if (i <= s_r) and sufficient_len(s_r) and (s[s_r:s_r + m] == r):

            # Add string before removed pattern
            modified += s[i : s_r]
            i = s_r + m
            print(s_r, "modified", modified)

    if i < n:
        # Add remaining string s back to modified string
        modified+= s[i:]

    print("withoutString(\"{}\", \"{}\") = {}".format(s, r, modified))
    return modified

if __name__ == "__main__":

    withoutString("Hello there", "llo")
    withoutString("Hello there", "e")
    withoutString("Hello there", "x")
    withoutString("xxx", "xx")
