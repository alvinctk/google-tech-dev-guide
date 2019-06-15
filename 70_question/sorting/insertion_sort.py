# O(n^2) time | O(1) space
def insertion_sort(a):
    i, n = 1, len(a)
    while i < n:
        j = i - 1
        while j >= 0 and a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
        i += 1
    return a

if __name__ == "__main__":
   x = [8, 5, 2, 9, 5, 6, 3]
   print("Array before sorted: {}".format(x))
   insertion_sort(x)
   print("Array after sorted: {}".format(x))
