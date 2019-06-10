class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.height = -1

    def __str__(self):
        return str(self.data)


class AVL_Tree:

    ALLOWED_IMBALANCE = 1

    def __init__(self):
        """
        Initialize AVL_TREE
        """
        self.root = None
        self.height = -1

    def get_height(self, t: Node):
        """
        Returns the height of a given node t
        """
        return -1 if t is None else t.height

    def set_height(self, t: Node):
        """
        Set height for a given node t.
        If node has no children, then height = 0
        If node has 1 layer children, then height = 1
        """
        h = self.get_height
        t.height = max(h(t.left), h(t.right)) + 1

    def find_max(self):
        """
        Returns the maximum value for the whole tree. Otherwise, returns
        None if empty.
        """
        return self.find_max_value(self.root)

    def find_max_value(self, t: Node):
        """
        Returns the maximum value for a subtree/tree. Otherwise, returns
        None if empty
        """
        if t is None:
            return None
        current = t
        while (current.right is not None):
            current = current.right
        return current.data

    def find_min(self):
        """
        Returns the minimum value for the whole tree. Otherwise, returns
        None if empty.
        """
        return self.find_min_value(self.root)

    def find_min_value(self, t: Node):
        """
        Returns the minimum value for a subtree/tree. Otherwise, returns
        None if empty
        """
        if t is None:
            return None
        current = t
        while (current.left is not None):
            current = current.left
        return current.data

    def contains(self, value):
        """
        Returns True if value contains in binary tree.
        Otherwise, returns False if value does not contains in binary tree.
        """
        return self.contains_value(value, self.root)

    def contains_value(self, value, node):
        """
        Recursive helper function to check if a value contains in binary tree.
        """
        if node is None:
            return False

        if node.data < value:
            return self.contains_value(value, node.left)
        elif node.data > value:
            return self.contains_value(value, node.right)
        else:
            return True

    def insert(self, value):
        """
        Insert value into AVL binary Tree by creating a node
        """
        if self.root is None:
            self.root = Node(value, None, None)
        else:
            self.root = self.insert_value(value, self.root)

    def insert_value(self, value, t: Node):
        """
        Recursive helper to insert value into AVL binary Tree and
        then rebalance the tree for each insert.
        """
        if t is None:
            t =  Node(value, None, None)
        elif value < t.data:
            t.left = self.insert_value(value, t.left)
        elif value > t.data:
            t.right = self.insert_value(value, t.right)
        # else: # Duplicate, do nothing.

        return self.balance(t)

    def remove(self, value):
        """
        Remove a value from the AVL binary tree
        """
        self.root = self.remove_value(value, self.root)

    def remove_value(self, value, t: Node):
        """
        Recursive helper to remove a value from the AVL binary tree; and,
        Updates and rebalance the tree.
        """
        if t is None:
            # Item not found, do noting
            return t
        if value < t.data:
            t.left = self.remove_value(value, t.left)
        elif value > t.data:
            t.right = self.remove_value(value, t.right)
        elif t.left is not None and t.right is not None:
            # Two children
            t.data = self.find_min_value(t.right)

            # Replace current value by the smallest value of the right
            # subtree.
            t.data = self.find_min_value(t.right)

            # Remove the smallest value of the right subtree since its value
            # has been copied to the node to be removed.

            # Since the smallest value node, it has either 0 or 1 children.
            t.right = self.remove_value(t.data, t.right)
        else:
            # either one child or no child
            # One or zero children
            if t.left is not None:
                t = t.left
            else:
                # right can be null or has value
                t = t.right
        return self.balance(t)

    def not_balance(self, x: Node, y: Node):
        """
        Return whether for child at Node x is not balance.
        """
        h = self.get_height
        return (h(x) - h(y)) > self.ALLOWED_IMBALANCE

    def balance(self, t: Node):
        """
        Balance the AVL binary tree
        """
        if t is None:
            return t

        h = self.get_height

        if self.not_balance(t.left, t.right):
            if h(t.left.left) >= h(t.left.right):
                # Case 1
                t = self.rotate_with_left_child(t)
            else:
                # Case 2
                t = self.double_with_left_child(t)

        elif self.not_balance(t.right, t.left):
            if h(t.right.right) >= h(t.right.left):
                # Case 4
                t = self.rotate_with_right_child(t)
            else:
                # Case 3
                t = self.double_with_right_child(t)

        self.set_height(t)

        return t

    def rotate_with_left_child(self, k2: Node):
        """
        Case 1: An insertion onto left subtree of left child of k2
        To fix case 1: Rotate with left child (or single right rotation)

           k2             Right         k1
          / \            Rotation     /   \
        k1   Z           ---->            k2
        /\                          /     /\
       /  Y                        X     Y  Z
      X
      """
        k1 = k2.left         # Keep a reference to k1
        k2.left = k1.right   # k2.left = Y
        k1.right = k2
        self.set_height(k2)
        self.set_height(k1)
        return k1

    def rotate_with_right_child(self, k2: Node):
        """
        # Case 4: An insertion onto right subtree of right child of k2
        # To fix case 4: Rotate with left child (or single left rotation)
        #
           k2             Left          k1
          /  \            Rotation     /   \
         Z    K1           ---->      k2
             / \                     / \     \
            Y   \                   Z  Y      X
                 X
      """
        k1 = k2.right         # Keep a reference to k1
        k2.right = k1.left    # k2.right = Y, to remove k1.left
        k1.left = k2
        self.set_height(k2)
        self.set_height(k1)
        return k1

    def double_with_left_child(self, k3: Node):
        """
        Double rotate binary tree node: first left child with its right child;
        then node k3 with new left child.
        Case 2: An insertion onto right substree of the left child of k3
        To fix case 2: Left-right rotation => Double rotation
        #

           k3            Left-Right     k1
          / \            Rotation     /   \
        k1   D           ---->            k2
        /\                          /     /\
       A  k2                        x     Y  Z
          / \
         B   C
                     Left Rotation
        k1              ---->        k2       --->     k2
        /\                          /                  / \
       A  k2                       k1                 k1  C
          / \                      /                  / \
         B   C                    A                   A  B

        k3
        / \            Right Rotation   k2       ---->      k2
       k2  D              ---------->   / \                /   \
                                          k3              k1    k3
                                            \             /\    / \
                                             D           A B    C  D
        """
        # To left rotate on k1 = k3.left node
        k3.left = self.rotate_with_right_child(k3.left)
        # To right rotate on k3 node
        return self.rotate_with_left_child(k3)

    def double_with_right_child(self, k3: Node):
        """
        Double rotate binary tree node: first right child with its left child;
        then node k3 with new right child.

        Case 3: An insertion onto left substree of the right child of k3
        To fix case 3: right-left rotation => Double rotation
        Diagram similar to case 2.
        """
        k3.right = self.rotate_with_left_child(k3.right)
        # To left rotate on k3 node
        return self.rotate_with_right_child(k3)

    def print_tree(self, ascending=True):
        """
        To print tree value.
        """
        self.print_tree_value(self.root, ascending)

    def print_tree_value(self, node, ascending=True):
        """
        Recursive helper to print tree value.
        By default in ascending order: left, center, right.
        To print in descending order, set ascending = False.
        descending order: right, center left
        """
        # Base case is implicitly to do nothing on null
        if node is not None:
            if ascending:
                # Ascending order
                # Recursive case: print left, center, right
                self.print_tree_value(node.left, ascending)
                print(node.data, end=" ")
                self.print_tree_value(node.right, ascending)
            else:
                # Descending order
                # Recursive case: print right, center, left
                self.print_tree_value(node.right, ascending)
                print(node.data, end=" ")
                self.print_tree_value(node.left, ascending)

    def display(self):
        """
        To display tree in layers
        """
        if self.root is None:
            return
        lines, _, _, _ = self.display_aux(self.root)
        for line in lines:
            print(line)

    def display_aux(self, node:Node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display_aux(node.left)
        right, m, q, y = self.display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def test_print(values, contains, remove):
    """
    To test the functions of binary tree
    """
    #print("args = ", args)
    avl = AVL_Tree()
    for x in values:
        avl.insert(x)
        print("inserting: ", x)
        avl.display()

    print(end="")
    print("The following values are inserted into tree:", values)
    print("Tree in ascending order:", end=" ")
    avl.print_tree()
    print("\nTree in descending order:", end=" ")
    avl.print_tree(ascending=False)
    print("\nRemoving {}:".format(remove), end=" ")
    avl.remove(remove)
    avl.print_tree()
    print()
    avl.display()

    print("\nroot =", avl.root)
    if avl.root is not None:
        print("root.left =", avl.root.left)
        print("root.right =", avl.root.right)
    print("tree's min value =", avl.find_min())
    print("tree's max value =", avl.find_max())
    for c in contains:
        print("does {} contains in tree = {}".format(c, avl.contains(c)))
    print()
if __name__ == "__main__":
    c = [10, 20, 30, 40, 50, 25]
    b = [6, 2, 8, 1, 5, 3, 4]
    x = [1, 2, 4, 8, 8, 10, 9]
    y = [12, 6, 14, 3]
    z = [3]
    a = []

    for values, remove in zip([c, b, x, y, z, a], [30, 2, 4, 6, 3, 0]):
        test_print(values, [5, 10, 2], remove)
