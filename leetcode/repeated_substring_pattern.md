# Repeated substring pattern

The technique of repeated substring pattern is used to solve the original problem. 


## Original problem

[LeetCode problem: Encode string with shortest length](https://leetcode.com/problems/encode-string-with-shortest-length)

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

- k will be a positive integer and encoded string will not be empty or have extra space.
- You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
- If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
Either don't encode s at all, or encode it as one part k[...] or encode it as multiple parts (in which case we can somewhere split it into two subproblems). Whatever is shortest. Uses @rsrs3's nice trick of searching s in s + s.

## Solution to solve original problem

**Python 3**
```python
def encode(self, s: str, memo={}) -> str:
    
if s not in memo:
        
        n = len(s)
        i = (s + s).find(s, 1)
        
        one = "{}[{}]".format(n//i, self.encode(s[:i])) if i < n else s
        multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
        memo[s] = min([s, one] + multi, key=len)
        print("i={}, one={}, multi={}, memo[{}]={}".format(i, one, multi, s, memo[s]))
    return memo[s]
```

```
Example 1: 

input = "aaa"

stdout:
i=1, one=a, multi=[], memo[a]=a
i=1, one=2[a], multi=['aa'], memo[aa]=aa
i=1, one=3[a], multi=['aaa', 'aaa'], memo[aaa]=aaa

output:
"aaa"

Example 2:
input= "aaaaaaaaaa"

stdout:
i=1, one=a, multi=[], memo[a]=a
i=1, one=2[a], multi=['aa'], memo[aa]=aa
i=1, one=3[a], multi=['aaa', 'aaa'], memo[aaa]=aaa
i=1, one=4[a], multi=['aaaa', 'aaaa', 'aaaa'], memo[aaaa]=aaaa
i=1, one=5[a], multi=['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa'], memo[aaaaa]=5[a]
i=1, one=6[a], multi=['a5[a]', 'aaaaaa', 'aaaaaa', 'aaaaaa', '5[a]a'], memo[aaaaaa]=6[a]
i=1, one=7[a], multi=['a6[a]', 'aa5[a]', 'aaaaaaa', 'aaaaaaa', '5[a]aa', '6[a]a'], memo[aaaaaaa]=7[a]
i=1, one=8[a], multi=['a7[a]', 'aa6[a]', 'aaa5[a]', 'aaaaaaaa', '5[a]aaa', '6[a]aa', '7[a]a'], memo[aaaaaaaa]=8[a]
i=1, one=9[a], multi=['a8[a]', 'aa7[a]', 'aaa6[a]', 'aaaa5[a]', '5[a]aaaa', '6[a]aaa', '7[a]aa', '8[a]a'], memo[aaaaaaaaa]=9[a]
i=1, one=10[a], multi=['a9[a]', 'aa8[a]', 'aaa7[a]', 'aaaa6[a]', '5[a]5[a]', '6[a]aaaa', '7[a]aaa', '8[a]aa', '9[a]a'], memo[aaaaaaaaaa]=10[a]

output= "10[a]"
```

**Python 2:**
```python
def encode(self, s, memo={}):
    if s not in memo:
        n = len(s)
        i = (s + s).find(s, 1)
        one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
        multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in xrange(1, n)]
        memo[s] = min([s, one] + multi, key=len)
    return memo[s]
```

## Basic idea using repeated substring pattern to solve the original problem 

Basic idea from [here](https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/easy-python-solution-with-explaination):
1. First char of input string is first char of repeated substring

2. Last char of input string is last char of repeated substring

3. Let S1 = S + S (where S in input string)

4. Remove 1 and last char of S1. Let this be S2

5. If S exists in S2 then return true else false

6. Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

```python
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

```python
def repeatedSubstringPattern(self, str):
    return str in (2 * str)[1:-1]
```

The explanation for why that works is pretty straight forward.

Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.

Fine. How do we apply that to this problem? We consider every rotation of string S such that it's rotated by k units [k < len(S)] to the left. Specifically, we're looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...

If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times), then we can check if the string is equal to some rotation of itself, and if it is, then we know that the string is periodic. Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S).

## Another simply explanation:
```python
ss = (s + s)[1:-1]
return ss.find(s) != -1
```

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
 
## [Rigorous proof: Why condition "(s+s).find(s,1) < s.size()" is equivalent to substring repetition?](https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95601/Rigorous-proof%3A-Why-condition-%22(s%2Bs).find(s1)-less-s.size()%22-is-equivalent-to-substring-repetition)


Why condition (s+s).find(s,1) < s.size() is equivalent to substring repetition?

Proof: Let N = s.size() and L := (s+s).find(s,1), actually we can prove that the following 2 statements are equivalent:

    1. 0 < L < N;
    2. N%L == 0 and s[i] == s[i%L] is true for any i in [0, N). 
       (which means s.substr(0,L) is the repetitive substring)


Consider function char f(int i) { return s[i%N]; }, obviously it has a period N.

**"1 => 2"**: From condition 1, we have for any i in [0,N)

    - `s[i] == (s+s)[i+L] == s[(i+L)%N]`,
    which means L is also a positive period of function f. Note that N == L*(N/L)+N%L, so we have
    
    - `f(i) == f(i+N) == f(i+L*(N/L)+N%L) == f(i+N%L)`,
    which means N%L is also a period of f. Note that N%L < L but L := (s+s).find(s,1) is the minimum positive period of function f, so we must have N%L == 0. Note that `i == L*(i/L)+i%L`, so we have

    - `s[i] == f(i) == f(L*(i/L)+i%L) == f(i%L) == s[i%L]`, so condition 2 is obtained.

**"2=>1"**: If condition 2 holds, for any i in [0,N), note that N%L == 0, we have

    - `(s+s)[i+L] == s[(i+L)%N] == s[((i+L)%N)%L] == s[(i+L)%L] == s[i]`, which means `(s+s).substr(L,N) == s`, so condition 1 is obtained.
