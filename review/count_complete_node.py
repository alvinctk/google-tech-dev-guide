class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def count(node: TreeNode) -> int:
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)

        def height(node: TreeNode) -> int:
            if not node:
                return 0
            elif not node.left:
                return 1
            else:
                return 1 + height(node.left)

        def count_complete(node: TreeNode) -> int:
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == right:
                return (1 << left) + count_complete(node.left)
            else:
                return (1 << right) + count_complete(node.right)

        return count_complete(root) - 1


