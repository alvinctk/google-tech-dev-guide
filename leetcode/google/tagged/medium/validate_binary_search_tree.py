from typing import NewType

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


Node = NewType("Node", TreeNode)

class Solution(object):
    def isValidBST(self, root: Node):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(N) since visited each node exactly once.
        Space complexity: O(N)
        """
        def helper(node, lower, upper):
            if not node:
                return True

            if node.val <= lower or upper <= node.val:
                return False

            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True

        lower, upper = float("-inf"), float("inf")
        return helper(root, lower, upper)

class Solution2:
    def isValidBST(self, root: Node) -> bool:
        """
        Approach 2: Iteration
        Time complexity: O(N) since visited each node exactly once
        Space complexity: O(N) to store each node's range limit data exactly once
        """
        if not root:
            return True

        q = [(root, float("-inf"), float("inf"))]
        while q:
            root, lower, upper = q.pop()
            if not root:
                continue
            if root.val <= lower or root.val >= upper:
                return False
            q.append((root.left, lower, root.val))
            q.append((root.right, root.val, upper))

        return True

class Solution3:
    def isValidBST(self, root: Node) -> bool:
        """
        Approach 3: In order traversal
        Time complexity: O(N) worse case when BST or the "bad" element is a rightmost leaf
        Space complexity: O(N) to keep stack trace
        """

        previous, q = float("-inf"), []
        while q or root:
            while root:
                q.append(root)
                root = root.left
            root = q.pop()
            if root.val <= previous:
                return False
            previous = root.val
            root = root.right
        return True

