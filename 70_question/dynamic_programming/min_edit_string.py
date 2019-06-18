# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    m, n = len(str1), len(str2)
    if m == 0:
        return n
    if n == 0:
        return m

    # matrix (row=n, column=m)
    d = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i
            elif str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i-1][j], # Insert/cell above
                                  d[i][j-1],     # Remove/cell left
                                  d[i-1][j-1])   # Replace/cell diagonal

    print("The minimum number of edit operations on str1=\"{}\" to obtain str2=\"{}\" = {}"
          .format(str1, str2, d[-1][-1]))
    return d[-1][-1]

if __name__ == "__main__":
    levenshteinDistance("abc", "yabd")


