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
    """
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def make_empty(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def contains(self, value):
        return self.contains_value(value, self.root)

    def contains_value(self, value, node):
        if node is None:
            return False

        if node.value < value:
            return self.contains_value(value, node.left)
        elif node.value > value:
            return self.contains_value(value, node.right)
        else:
            return True

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

def test_print(values, *args):
    """
    To test the functions of binary tree
    """
    #print("args = ", args)
    bt = Binary_Tree()
    for x in values:
        bt.insert(x)

    print("The following values are inserted into tree:", values)
    print("Tree in ascending order:")
    bt.print_tree()

    print("\nTree in descending order:")
    bt.print_tree(ascending=False)

    print("\nroot =", bt.root)
    print("root.left =", bt.root.left)
    print("root.right =", bt.root.right)

    for c in args:
        print("does {} contains in tree = {}".format(c, bt.contains(c)))

if __name__ == "__main__":
    x = [2, 4, 1, 8, 8, 10, 9]
    y = [12, 6, 14, 3]
    for values in [x, y]:
        print()
        test_print(values, 5, 10, 2)
