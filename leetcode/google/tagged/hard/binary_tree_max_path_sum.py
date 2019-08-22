# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Either traversal is fine - preorder (left, right, node) or postorder (right, left, node).
        Recursion approach to compute the max path at tail-end of recursion call.

        The maximum triangle path sum may formed by
        either from a triangle (left, node, right)
        or from a single combination of right/left child
        or from a single node
        """
        def mps(node: TreeNode) -> (int, int):
            if not node:
                # Possible to allow negative num to be maximum
                return (float("-inf"), float("-inf"))

            # left triangle sum, left node child sum
            lts, lns = mps(node.left)

            # right triangle sum, right node child sum
            rts, rns = mps(node.right)

            # node sum
            val = node.val

            # single child sum
            sc = max(lns, rns)

            # node child sum
            ns = max(val, val + sc)

            # node triangle sum
            ts = max(ns, val + lns + rns)

            # maximum triangle sum
            mts = max(ts, lts, rts)

            # To prevent from getting multiple triangle
            # Allow only a single connection from a node
            # maximum triangle sum or node child sum
            return mts, ns
        max_path_sum, max_node_sum = mps(root)
        return max_path_sum



