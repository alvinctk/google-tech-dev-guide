"""
Using an implicit memorization approach by using a dictionary as cache
"""
fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the Nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the fibonacci value
    fibonacci_cache[n] = value

    return value

if __name__ == "__main__":
    for n in range(1, 1001):
        print(n, ":", fibonacci(n))
