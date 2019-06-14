from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if type(n) is not int:
        raise TypeError("n must be positive int")
    if n < 0:
        raise ValueError("n must be a positive int")

    if n == 0 or n == 1:
        return 1
    elif n >= 2:
        return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    for n in range(1, 20):
        print(n, ":", fibonacci(n))

