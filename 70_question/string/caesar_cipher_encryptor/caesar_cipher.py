from string import ascii_lowercase as letters
def caesar_cipher_encryptor(s, k):
    """
    s string to encrpyt
    k number to shift left by
    """
    n = len(letters)
    k = k % n
    result = []
    for c in s:
        shift = (ord(c) - ord("a") + k) % n
        result.append(letters[shift])
    return "".join(result)

if __name__ == "__main__":
    s, k = "xyz", 2
    print("{} shift left by {} = {}".format(s, k, caesar_cipher_encryptor(s, k)))


