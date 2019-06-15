def print_palindrome(s, palindrome):
    print("The largest palindrome substring in \"{}\" is \"{}\"".format(s, palindrome))

def longestPalindromicSubstring(string):
    n = len(string)
    if n <= 2:
        palindrome = ""
        if n <= 1 or (n == 2 and string[0] == string[1]):
            palindrome = string
        print_palindrome(string, palindrome)
        return palindrome

    s = "^" + string[0]
    for x in string[1:]:
        s += "#"
        s += x
    s += "$"
    m = len(s)
    c = 3
    max_substring = string[0]
    #print(s)
    while c < m - 2:
        l, r = c, c
        count = 0
        if s[c] == "#":
            l -= 1
            r += 1
        else:
            l -= 2
            r += 2
        #print(string, n, s, m,  "c=", c, s[c], "l=", l, s[l], "r=", r, s[r])
        while r + 2 < m and s[l] == s[r] and s[l] != s[0]:
            #print("s={}, l={}, c={}, r={}, m={}, s[l:r]={}".format(s, l, c, r, m, s[l:r]))
            l -= 2
            r += 2
            count += 1
        #print("count", l, r)
        if s[l] == s[r] or count:

            #print("s={}, l={}, c={}, r={}, s[l:r]={}".format(s, l, c, r, s[l:r]))
            if s[l] != s[r]:
                l, r = l + 2, r - 2
            length = (r - l)/2 + 1
            if length > len(max_substring):
                max_substring = string[(l-1)//2:(r-1)//2+1]
                #print(max_substring)
        c += 1

    print_palindrome(string, max_substring)
    return max_substring

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        return True
if __name__ == "__main__":
    a = "abcdefghfedcbaa"
    x = "abc"
    y = "it's highnoon"
    for c in [a, x, y]:
        longestPalindromicSubstring(c)

