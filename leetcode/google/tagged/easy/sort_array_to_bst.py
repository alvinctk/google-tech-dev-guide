from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Time complexity = O(n log n)
        Space complexity = O(log n) depth of the recursive stack

        Runtime: 72 ms, faster than 94.13% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
        Memory Usage: 16.4 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
        """
        def BST(left, right):
            if left > right:
                return None

            mid = left + (right - left)//2
            node = TreeNode(nums[mid])
            node.left = BST(left, mid - 1)
            node.right = BST(mid + 1, right)

            return node

        return BST(0, len(nums)-1)
