# O(n) time and O(n) space
# O(n) array space + O(log n) stack heap space is bounded by O(n)
def inOrderTraverse(tree, array):
    # left, root, right
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

# O(n) time and O(n) space
# O(n) array space + O(log n) stack heap space is bounded by O(n)
def preOrderTraverse(tree, array):
    if tree:
        # root, left, right
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# O(n) time and O(n) space
# O(n) array space + O(log n) stack heap space is bounded by O(n)
def postOrderTraverse(tree, array):
    if tree:
        # left, right, root
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
