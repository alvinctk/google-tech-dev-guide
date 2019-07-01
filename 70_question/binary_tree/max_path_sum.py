# O(n) time and O(log n) space
def max_path_sum(tree):
    _, max_path_sum = max_path_sum_helper(tree)
    return max_path_sum

def max_path_sum_helper(tree):
    if not tree:
        # Base case of not a node
        return (0, 0)

    # Depth first bottom up approach to calculate the max path sum
    left_branch_sum, left_triangle_sum  = max_path_sum_helper(tree.left)
    right_branch_sum, right_triangle_sum = max_path_sum_helper(tree.right)

    # Using node label instead of tree seems to be more appropriate
    node_value = tree.value

    # The max between left or right
    child_branch_sum = max(left_branch_sum, right_branch_sum)

    # The max from either node, node + left, or node + right
    node_child_sum = max(node_value + child_branch_sum, node_value)

    # The max sum may comes a triangle (left - Node - right)
    # or either node or node - left or node - right
    triangle_sum = max(node_child_sum, left_branch_sum + node_value + right_branch_sum)

    # Only one triangle is allowed since maximum connection between a node is two.
    # Since the maximum path sum can only exist one triangle being formed, then
    # the triangle might come from the current node triangle, left triangle, or right triangle.
    max_path_sum = max(triangle_sum, left_triangle_sum, right_triangle_sum)

    # Returns to the parent node in order to compute a valid path to avoid multiple triangles.
    # That is, return (max sum that does not form a triangle, max sum possibly formed by a triangle)
    return node_child_sum, max_path_sum
