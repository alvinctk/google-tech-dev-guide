def findThreeLargestNumbers(array):
    reassign(array)
    third_biggest, i, n = 0, 3, len(array)
    while i < n:
        if array[i] >= array[third_biggest]:
            array[i], array[third_biggest] = array[third_biggest], array[i]
            reassign(array)
        i += 1
    reassign(array)
    return array[:3]

def reassign(a, largest=True):
    x, y, z = 0, 1, 2
    f = lambda g, h, j: a[g] <= a[h] and a[h] <= a[j]
    r = lambda g, h, j: (a[g], a[h], a[j])

    if f(z, y, x):
        a[:z+1] = r(z, y, x)
    elif f(z, x, y):
        a[:z+1] = r(z, x, y)
    elif f(y, z, x):
        a[:z+1] = r(y, z, x)
    elif f(y, x, z):
        a[:z+1] = r(y, x, z)
    elif f(x, z, y):
        a[:z+1] = r(x, z, y)

if __name__ == "__main__":
    x = [49, 1, 3, 4, 50, 60]
    print("Largest three of", x, "=", findThreeLargestNumbers(x))
