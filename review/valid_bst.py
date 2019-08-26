class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Time complexity: O(N) since each node is visited exactly once.
        Space complexity: O(N) keep entire tree
        """
        def helper(node, lower, upper):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not helper(node.left, lower, node.val):
                return False

            if not helper(node.right, node.val, upper):
                return False

            return True

        lower, upper = float("-inf"), float("inf")
        return helper(root, lower, upper)
