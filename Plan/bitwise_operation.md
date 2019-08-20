## Bitwise operations

n = the bit number
0 = the least significant bit 

- Set a bit 
```
x |= (1 << n)
```
- ### Clear a bit
```
x &= ~(1 << n)
```

- Toggle a bit 
```
x ^= (1 << n)
```

- Test a bit
```
y = x & (1 << n)
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
