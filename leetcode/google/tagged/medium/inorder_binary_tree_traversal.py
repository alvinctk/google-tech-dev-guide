from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Time complexity: O(N) since visit exactly N nodes once.
        Space complexity: O(N) for skew binary tree; O(log N) for balance binary tree.
                          Space due to recursive depth stack space
        Runtime: 32 ms, faster than 92.54% of Python3 online submissions for Binary Tree Inorder Traversal.
        """
        def values(node: TreeNode, nums: List[int]) -> List[int]:
            if not node:
                return nums
            values(node.left, nums)
            nums.append(node.val)
            values(node.right, nums)
            return nums
        return values(root, [])
