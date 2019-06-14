from functools import lru_cache

@lru_cache(100)
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield i, a
        a, b = b, a + b

if __name__ == "__main__":
    for i, x in fibonacci(100):
        print(i, ":", x)
