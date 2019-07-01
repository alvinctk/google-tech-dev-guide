def invert_binary_tree(tree):
    # To test both functions at the same time
    invert_binary_tree_recursive(tree)
    invert_binary_tree_iterative(tree)
    invert_binary_tree_recursive(tree)

# O(n) time and O(n) space
def invert_binary_tree_iterative(tree):
    q = [tree]
    while q:
        node = q.pop(0)
        node.left, node.right = node.right, node.left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# O(n) time and O(log n) space. Space in the stack frame.
def invert_binary_tree_recursive(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invert_binary_tree_recursive(tree.left)
        invert_binary_tree_recursive(tree.right)

