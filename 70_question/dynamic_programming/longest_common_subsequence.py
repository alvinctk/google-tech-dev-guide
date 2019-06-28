# Optimal Solution
# O(nm) time and O(nm) space where n is length of a and m is length of b
def longestCommonSubsequence(a, b, debug=False):
    """
    Storing the length of LCS at each i, j index in an array of LCS length
    Backtrack to construct a LCS string
    """
    # Compute the length of LCS at a given index i, j
    # All values in row 0 contains length of 0 since empty "" against b[i].
    # All values in column 0 contains length 0 since empty "" against a[i]
    n, m = len(a), len(b)
    L = [[0]*(m+1) for _ in range(n+1)]
    i, j = 1, 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                L[i][j] = 1 + L[i-1][j-1]

            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # Backtrack to construct LCS string
    i, j = n, m
    k = L[-1][-1] - 1
    s = [""] * L[-1][-1]
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            s[k] = a[i-1]
            i -= 1
            j -= 1
            k -= 1
        elif L[i][j-1] > L[i-1][j]:
            j -= 1
        else:
            i -= 1

    if debug:
        print("Length array:")
        for row in L:
            for item in row:
                print(item, end=" ")
            print(end="\n")

        print(s)

    print_result(a, b, "".join(s))
    return s


# O(nm* min(n,m)) time and O(nm* min(n,m)) space where n is length of a and m is length of b
# Where min(n, m) denotes the time/space it takes to concat a string
def longestCommonSubsequence2(a, b, debug=False):
    """
    Bottom approach, Dynamic programming.
    Storing each LCS string at each i, j index in an array of LCS sequence
    """


    # Compute the length of LCS at a given index i, j
    # All values in row 0 contains length of 0 since empty "" against b[i].
    # All values in column 0 contains length 0 since empty "" against a[i]
    n, m = len(a), len(b)
    L = [[0]*(m+1) for _ in range(n+1)]
    s = [[""]*(m+1) for _ in range(n+1)]
    i, j = 1, 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                if debug: L[i][j] = 1 + L[i-1][j-1]
                s[i][j] = s[i-1][j-1] + a[i-1]

            else:
                if debug: L[i][j] = max(L[i-1][j], L[i][j-1])
                s[i][j] = max(s[i-1][j], s[i][j-1], key=len)

    if debug:
        print("Length array:")
        for row in L:
            for item in row:
                print(item, end=" ")
            print(end="\n")

        t = L[n][m]
        print("LCS array:")
        for i, row in enumerate(s):
            for j, item in enumerate(row):
                if i == 0 or j == 0:
                    continue
                print(item.rjust(t, " "), end=" ")
            print(end="\n")

    print_result(a, b, s[-1][-1])
    return list(s[-1][-1])

def print_result(a, b, r):
    print("The longest common subsequence (LCS) of \"{}\" and \"{}\" is \"{}\".".format(a, b, r))

if __name__ == "__main__":
    x = "ZXVVYZW"
    y = "XKYKZPW"
    longestCommonSubsequence(x, y)
    longestCommonSubsequence("ABCDEFG", "APPLES")

