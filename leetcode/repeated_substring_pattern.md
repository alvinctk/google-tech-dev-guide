# Repeated substring pattern

Basic idea from [here](https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/easy-python-solution-with-explaination):
1. First char of input string is first char of repeated substring

2. Last char of input string is last char of repeated substring

3. Let S1 = S + S (where S in input string)

4. Remove 1 and last char of S1. Let this be S2

5. If S exists in S2 then return true else false

6. Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

```
def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
        ss = (str + str)[1:-1]
        return ss.find(str) != -1
```

But the code can be nicer, at least better use the in operator:

```
def repeatedSubstringPattern(self, str):
    return str in (2 * str)[1:-1]
```

The explanation for why that works is pretty straight forward.

Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.

Fine. How do we apply that to this problem? We consider every rotation of string S such that it's rotated by k units [k < len(S)] to the left. Specifically, we're looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...

If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times), then we can check if the string is equal to some rotation of itself, and if it is, then we know that the string is periodic. Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S).

## Another simply explanation:

ss = (s + s)[1:-1]
return ss.find(s) != -1

The maximum length of a "repeated" substring that you could get from a string would be half it's length
For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
You cannot have a substring >(len(s)/2), that can be repeated.

1. So, when ss = s + s , we will have at least 4 parts of "repeated substring" in ss.
2. (s+s)[1:-1], With this we are removing 1st char and last char => Out of 4 parts of repeated substring, 2 part will be gone (they will no longer have the same substring).

3. ss.find(s) != -1, But still we have 2 parts out of which we can make s. And that's how ss should have s, if s has repeated substring.


## Alternative

If the string S has repeated block, it could be described in terms of pattern.
S = SpSp (For example, S has two repeatable block at most)
If we repeat the string, then SS=SpSpSpSp.
Destroying first and the last pattern by removing each character, we generate a new S2=SxSpSpSy.

If the string has repeatable pattern inside, S2 should have valid S in its string

## Proof 
I would try to propose a more strict proof idea:
It's obvious that valid string will be captured by this algorithm, but why invalid one return false is not intuitive.
From the algorithm, we can conclude that S satisfies that s = AB = BA (by AB, I mean s = the concatenation of A and B).
What I want to prove is if AB = BA, then there is a D such that A = n*D, B = m*D
Suppose len(A) = a, len(B) = b. Two cases:

1. If a = b or a = 1 or b = 1, the problem is trivial.
2. Without loss of generality, we could suppose that a < b.
 - According to AB = BA, we have A = B[1~a], which means that B = AC.
 - Then AB = BA ==> AAC = ACA and the problem size has been reduced from (a, b) to (a, b-a): AC = CA.
 - In the end, it will be reduced to one of the case in (1). Thus the problem is solved.
