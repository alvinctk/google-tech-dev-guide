## Bitwise operations

n = the bit number
0 = the least significant bit 

- Invert number/ 1's complement
```
num = 4 

```
- Set a bit 
```
x |= (1 << n)
```
- Clear a bit
```
x &= ~(1 << n)
```

- Toggle a bit 
```
x ^= (1 << n)
```

- Retrieve the rightmost/lowest set bit
Let X = 00101100. So ~X(1’s complement) will be ‘11010011’ and 2’s complement will be (~X+1 or -X) i.e  ‘11010100’.So if we ‘AND’ original number ‘X’ with its two’s complement which is ‘-X’, we get lowest set bit.
```
x = x  & (-x)_
```

- Remove the rightmost/lowest set bit
```
x = x  & (x - 1)_
```


- Test a bit
```
y = x & (1 << n)
```


- Test a number is odd or even
```
if x & 1:
    print("odd")
else:
    print("even")
```

- Swap two numbers without using a temporary variable
    - Using arithmetic operators
    ```
    # This works if x + y does not cause arithmetic overflow
    x, y = 10, 15
    x = x + y # Now x becomes 25
    y = x - y # Now y becomes 10
    x = x - y # Now x becoems 15
    ```

    - Bitwise XOR method
    ```
    x, y = 10, 15 # 10 = (1010), 15 = (1111)
    x = x ^ y # x becomes 5 (0101)
    y = x ^ y # y becomes 10 (1010)
    x = x ^ y # x becomes 15 (1111)
    ```

    - Above two methods fail when x and y points to the same object.
    ```
    # Bitwise XOR based method
    x = x ^ x; // x becomes 0
    x = x ^ x; // x remains 0
    x = x ^ x; // x remains 0

    # Arithmetic based method
    x = x + x; // x becomes 2x
    x = x – x; // x becomes 0
    x = x – x; // x remains 0
    ```
- count bits
```
def count_bits(x: int) ->:
    num_bits = 0 
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits
```

## Bitwise Examples: 
- `x | 2` is used to set bit 1 of `x` to 1
- `x & 1` is used to test if bit 0 of `x` is 1. 

## Sets

Sets can be combined using mathematical operations.

- The union operator | combines two sets to form a new one containing items in either.
- The intersection operator & gets items only in both.
- The difference operator - gets items in the first set but not in the second.
- The symmetric difference operator ^ gets items in either set, but not both.

```
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
```

```
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{4, 5, 6}
{1, 2, 3}
{8, 9, 7}
{1, 2, 3, 7, 8, 9}
```
