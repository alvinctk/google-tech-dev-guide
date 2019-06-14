def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    for n in range(1, 1001):
        print("fibonacci(n = {}) = {}".format(n, fibonacci(n)))
