"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach using hashtable

        Time complexity: O(n)
        Since, there will n insertion into the set/hash table.
        And, each insertion takes constant time.


        Space complexity: O(n). Space depends on number of elements in a list.

        Note:
        For not very large n, the runtime of this method can be slower than algorithm of O(n log n).
        The reason is hash table has some overhead maintaining its property.

        Big-O notation only tell us that for sufficiently large input, one will be faster than other.
        Therefore, when n is not sufficiently large, an O(n) algorithm can be slower than an O(n log n) algorithm.
        """

        return len(nums) > len(set(nums))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        Approach using sorting

        Time complexity: O(n log n).
        Sorting is O(n log n) and the sweeping is O(n).
        The entire algorithm is dominated by the sorting step which is O(n log n).

        Space complexity: O(1). Space depends on sorting implementation
        which usually cost O(1) auxillary space if heapsort is used.

        Note:
        The implementation here modifies the original array by sorting it.
        In general, it is not a good practice to modify the input unless it is clear to the caller
        that the input will be modified.
        One may make a copy of nums and operate on the copy instead.
        """
        nums.sort()
        i, n = 1, len(nums)
        previous = 0
        while i < n:
            if nums[i] == nums[previous]:
                return True
            else:
                previous = i
            i += 1
        return False
