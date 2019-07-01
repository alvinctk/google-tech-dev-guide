# Average time complexity O(log n)
# Worse time complexity O(n)
# Space complexity O(1)
def findClosestValueInBst(tree, target):
    current = tree
    closest = float("inf")
    while current:

        if abs(target - closest) > abs(target - current.value):
            closest = current.value

        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            return current.value

    return closest
