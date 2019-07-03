from typing import List
def reverse_string(s:List[str]) -> None:
    """
    To practice use of recursion
    """
    def helper(start, end):
        if start < end:
            s[start], s[end] = s[end], s[start]
            helper(start + 1, end - 1)

    print("before", s)
    n = len(s)
    if n > 1: helper(0, n - 1)
    print("after", s)

if __name__ == "__main__":
    reverse_string(["h", "e", "l", "l", "o"])
