

## [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)

> `itertools.product` computes the cartesian product of input iterables. 
It is equivalent to nested for-loops. 

For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
For example, product(A, B, C) returns the same as ((x, y, z) for x in A for y in B for z in C)

i[According to Python 3 itertools.product documentation](https://docs.python.org/3/library/itertools.html#itertools.product):
> Cartesian product of input iterables.
> 
> Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
> 
> The nested loops cycle like an odometer with the rightmost element advancing on every iteration. This pattern creates a lexicographic ordering so that if the input’s iterables are sorted, the product tuples are emitted in sorted order.
> 
> To compute the product of an iterable with itself, specify the number of repetitions with the optional repeat keyword argument. For example, product(A, repeat=4) means the same as product(A, A, A, A).
> 
> This function is roughly equivalent to the following code, except that the actual implementation does not build up intermediate results in memory:
 
```
 from itertools import product
 >>> list(product([1, 2, 3], repeat=2))
 [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)
```

```
 A = [[1, 2, 3], [3, 4, 5]]
 >>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
```

```
 >>> B = [[1,2,3],[3,4,5],[7,8]]
 >>> print list(product(*B))
 [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
```
