"""
Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr[i+1:] = arr[i:len(arr)-1]
                i += 2
            else:
                i += 1
        print(arr)

x = Solution()
x.duplicateZeros([])
x.duplicateZeros([1, 2, 3])
x.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
