from typing import List
class Solution:
    def findMedianSortedArrays(self, x: List[int], y: List[int]) -> float:
        if not x and not y:
            return 0

        def single_array_median(z: List[int]):
            n = len(z)
            mid = (n+1)//2 - 1
            if n % 2 == 1:
                return z[mid]
            else:
                return z[mid]/2 + z[mid+1]/2

        def x_p_one(x_p, y_p, x, y):
            print("in x_p_one")
            print("x_p=", x_p, "y_p=", y_p, x, y)
            if x[x_p] <= y[y_p+1]:
                if even:
                    max_left = max(x[x_p], y[y_p])
                    min_right = 0
                    if x_p + 1 == m:
                        min_right = y[y_p+1]
                    else:
                        min_right = min(y[y_p+1], x[x_p+1])
                    return (max_left + min_right)/2
                else:
                    return max(x[x_p], y[y_p])
            else:
                # x[x_p] > y[y_p+1]
                y_p += 1
                print("y_p += 1")
                #print("x_p=", x_p, "y_p=", y_p, x, y)
                #y_p_1 = min(y[y_p+1], x[x_p])
                #print(y_p_1, even)
                if even:
                    min_right = min(y[y_p + 1], x[x_p]) if y_p + 1 < n else x[x_p]
                    print(y[y_p], min_right, (y[y_p] + min_right)/2)
                    return (y[y_p] + min_right)/2
                else:
                    return y[y_p]

        if x and not y:
            return single_array_median(x)
        elif y and not x:
            return single_array_median(y)


        m, n = len(x), len(y)
        if m > n:
            x, y, m, n = y, x, n, m

        half = (n + m + 1)//2
        even = (n + m) % 2 == 0
        left = half//2
        x_p = left - 1 if left - 1 < m else m - 1
        y_p = half - (x_p + 1) - 1 if  half - (x_p + 1) > 0 else -1
        print("half", half, "even", even, "left", left, "xp", x_p, "yp", y_p)
        if m == 1:
            if n == 1:
                return (x[0] + y[0])/2
            else:
                return x_p_one(x_p, y_p, x, y)

        while 0 <= y_p + 1 < n:
            if x[x_p] <= y[y_p+1]:
                if x_p + 1 == m or (x_p + 1 < m and y[y_p] <= x[x_p + 1]):
                    break

            if x[x_p] > y[y_p+1]:
                x_p -= 1
                y_p += 1
                if x_p < 0:
                    x_p += 1
                    y_p -= 1
                    return x_p_one(x_p, y_p, x, y)

            if x_p + 1 < m and y[y_p] > x[x_p+1]:
                x_p += 1
                y_p -= 1

        max_left = 0
        if y_p == - 1:
            max_left = x[x_p]
        elif x_p == -1:
            max_left = y[y_p]
        else:
            max_left = max(x[x_p], y[y_p])

        min_right = 0
        #min(x[x_p + 1], y[y_p+1])
        if x_p + 1 < m and y_p + 1 < n:
            min_right = min(x[x_p+1], y[y_p+1])
        else:
            min_right = y[y_p + 1]
        if even:
            print("last even", max_left, min_right, x_p, y_p)
            return (max_left + min_right)/2
        else:
            print("last odd", max_left)
            return max_left

    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        #if n == 0:
        #    raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    def xfindMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #if not x and not y:
        #    return 0.0


        def single_array_median(array):
            l = len(array)
            mid = (l-1)//2
            print("mid", mid)
            if l - 1 % 2 == 0:
                return array[mid]
            else:
                return (array[mid] + array[mid+1])/2

        x, y = nums1, nums2
        n, m = len(nums1), len(nums2)

        if not x and y:
            return single_array_median(y)

        elif not y and x:
            return single_array_median(x)


        # +1 to offset to include the odd lengths
        # number of elements in left
        left = (n + m + 1)//2

        # _p ivot indicates pivot that represent all element to the right inclusive
        x_p = n - 1
        y_p = left - x_p - 1

        while 0 <= x_p - 1 < n and 0 <= y_p - 1 < m:
            if x[x_p-1] <= y[y_p] and y[y_p-1] <= x[y_p]:
                break
            if x[x_p-1] > y[y_p]:
                x_p -= 1
                y_p += 1
                continue

            if y[y_p-1] > x[x_p]:
                x_p += 1
                y_p -= 1
                continue

        left = x_p + y_p
        right = n + m - left

        remainder = right - left
        print(x_p, y_p)
        if (n+m) % 2 == 0:
            return (min(x[x_p] + y[y_p], x[x_p] + x[x_p+1] if x_p + 1 < n else float("inf"), y[y_p] + y[y_p+1] if y_p + 1 < m else float("inf")))/2
        else:
            return min(x[x_p], y[y_p])

if __name__ == "__main__":
    s = Solution()
    a = [[], [], [1], [1], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [1, 2, 3, 4], [4, 5, 8], [], [1], [1, 3], [1, 2], [], [1, 2], [1, 2], [2]]
    b = [[], [1], [], [2], [1], [7], [5, 7, 10, 11, 12, 13, 15], [1, 2, 3, 4, 5, 7], [1, 2, 3], [2, 3], [2], [3, 4, 5], [2, 3], [3], [3, 5], [1, 3, 4]]
    for x, y in zip(a, b):
        print(x, y, s.findMedianSortedArrays(x, y))
