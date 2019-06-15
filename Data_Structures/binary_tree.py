"""
Binary Tree
"""
class Binary_Node:
    """
    Binary Node class that creates a node object to be used in the Binary
    Tree structure.
    """
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def update(self, value, left, right):
        self.value =  value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class Binary_Tree:
    """
    Binary Tree class that handles the following operations:
        - is_empty => checks if the binary tree is empty
        - make_empty => reset the binary tree
        - contains(value) => find if a value contains in the tree
        - insert(value) => insert a value into the tree
        - print_tree => prints a tree in ascending order by default
        - find_min => returns min value if tree not empty. Otherwise, None.
        - find_max => returns max value if tree not empty. Otherwise, None.
    """
    def __init__(self):
        """
        Initialize root
        """
        self.root = None

    def get_root(self):
        """
        Return root
        """
        return self.root

    def make_empty(self):
        """
        Reset binary tree to empty
        """
        self.root = None

    def is_empty(self):
        """
        check if binary tree is empty
        """
        return self.root is None

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

        if node.value < value:
            return self.contains_value(value, node.left)
        elif node.value > value:
            return self.contains_value(value, node.right)
        else:
            return True

    def find_min(self):
        """
        Returns the minimum value for the whole tree. Otherwise, returns
        None if empty.
        """
        return self.find_min_value(self.root)

    def find_min_value(self, node):
        """
        Returns the minimum value for a subtree/tree. Otherwise, returns
        None if empty
        """
        if node is None:
            return None
        current = node
        while (current.left is not None):
            current = current.left
        return current.value

    def find_max(self):
        """
        Returns the maximum value if tree is not empty. Otherwise, returns
        None.
        """
        if self.root is None:
            return None
        current = self.root
        while (current.right is not None):
            current = current.right
        return current.value

    def remove(self, value):
        self.remove_value(value, self.root)

    def remove_value(self, value, node):
        """
        Recursive helper to remove element
        If the removal node has no children, simply remove the node.
        If the removal node has one children,
        """
        if node is None:
            return node
        if value < node.value:
            node.left = self.remove_value(value, node.left)
        elif value > node.value:
            node.right = self.remove_value(value, node.right)

        elif node.left is not None and node.right is not None:
            # Two children

            # Replace current value by the smallest value of the right
            # subtree.
            node.value = self.find_min_value(node.right)

            # Remove the smallest value of the right subtree since its value
            # has been copied to the node to be removed.

            # Since the smallest value node, it has either 0 or 1 children.
            node.right = self.remove_value(node.value, node.right)
        else:
            # One or zero children
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node
    def insert(self, value):
        """
        Insert value into Binary Tree by creating a binary node
        """
        if self.root is None:
            self.root = Binary_Node(value, None, None)
        else:
            self.insert_value(value, self.root)

    def insert_value(self, value, node):
        """
        Recursive helper function to insert value into binary tree
        """
        if value < node.value:
            # Insert value to left tree
            if node.left is None:
                node.left = Binary_Node(value, None, None)
            else:
                self.insert_value(value, node.left)
        else:
            # Insert value to right tree
            if node.right is None:
                node.right = Binary_Node(value, None, None)
            else:
                self.insert_value(value, node.right)

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
                print(node.value, end=" ")
                self.print_tree_value(node.right, ascending)
            else:
                # Descending order
                # Recursive case: print right, center, left
                self.print_tree_value(node.right, ascending)
                print(node.value, end=" ")
                self.print_tree_value(node.left, ascending)
    def display(self):
        lines, _, _, _ = self.display_aux(self.root)
        for line in lines:
            print(line)

    def display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.display_aux(node.left)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.display_aux(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display_aux(node.left)
        right, m, q, y = self.display_aux(node.right)
        s = '%s' % node.value
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
    bt = Binary_Tree()
    for x in values:
        bt.insert(x)
    print(end="")
    bt.display()
    print("The following values are inserted into tree:", values)
    print("Tree in ascending order:", end=" ")
    bt.print_tree()
    print("\nTree in descending order:", end=" ")
    bt.print_tree(ascending=False)
    print("Removing {}:".format(remove), end=" ")
    bt.remove(remove)
    bt.print_tree()
    print()
    bt.display()

    print("\nroot =", bt.root)
    if bt.root is not None:
        print("root.left =", bt.root.left)
        print("root.right =", bt.root.right)
    print("tree's min value =", bt.find_min())
    print("tree's max value =", bt.find_max())
    for c in contains:
        print("does {} contains in tree = {}".format(c, bt.contains(c)))
    print()
if __name__ == "__main__":
    b = [6, 2, 8, 1, 5, 3, 4]
    x = [1, 2, 4, 8, 8, 10, 9]
    y = [12, 6, 14, 3]
    z = [3]
    a = []
    for values, remove in zip([b, x], [2, 2]):
        print()
        test_print(values, [5, 10, 2], remove)
