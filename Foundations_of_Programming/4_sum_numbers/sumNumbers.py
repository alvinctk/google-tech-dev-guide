"""
problem
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)

sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
"""
import string
def sumNumbers(s):
    """
    Compute the sum of a number in a string
    s = string to compute number.
    """
    s = s.lower()
    strip_letters = lambda s: s.rstrip(" " + string.ascii_lowercase)
    strip_digits = lambda s: s.rstrip(string.digits)
    numbers = 0
    while len(s) > 0:
        # right strip any letters
        s = strip_letters(s)
        n = len(s)

        # Exit when there isn't any string left
        if n == 0:
            break
        # right strip any digits
        r = strip_digits(s)
        m = len(r)

        # number of digits to add to number
        offset = n - m
        if offset > 0:
            numbers += int(s[n-offset:])
        s = r
    print(numbers)
    return numbers

if __name__ == "__main__":
    sumNumbers("abc123xyz")
    sumNumbers("aa11bb33")
    sumNumbers("7 11")
