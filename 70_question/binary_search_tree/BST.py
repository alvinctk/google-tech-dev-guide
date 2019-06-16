class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self:
            self = BST(value)
            return self
        current = self
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right
        return self

    def contains(self, value):
        if not self:
            return False
        current = self
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def remove(self, value):
        #self = self.remove_value(value, self)
        self = self.remove_value_iteration(value, self)
        return self

    def remove_value_iteration(self, value, node):
        """
        Iteration helper to remove node
        If the removal node has no children, simply remove the node.
        If the removal node has one children, update the child to be node.
        If the removal node has two children, then update the node with
        smallest node in the right child subtree.
        """
        print("removing item", value)
        self.display()

        if self is None:
            return
        node, parent, direction  = self, self, "root"
        while node:
            if value < node.value:
                parent, direction = node, "left"
                node = node.left
            elif value > node.value:
                parent, direction = node, "right"
                node = node.right
            elif node.left is not None and node.right is not None:
                # Two children

                # Replace the current value by the smallest value of the right
                # subtree
                node.value = node.right.find_min_value()

                # Remove the smallest value of the right substree since its value
                # has been copied to the node to be removed.
                if node.value is None:
                    print("node value is none")
                elif node.right.value == node.value:
                    print("node.right.value == node.value")
                    self.display_aux(node.right)
                    node.right = node.right.right
                else:
                    current = node.right
                    while current:
                        print("current")
                        print(current.value, current.left.value, node.value)
                        self.display_aux(current)
                        if current.left and current.left.value == node.value:
                            current.left = current.left.right
                            break
                        current = current.left
                    self.display()
                    break
            else:
                print("one or zero children removing ", node.value)
                self.display_aux(node)
                # One or zero children
                if node.left is not None:
                    if direction == "root":
                        self = node.left
                    elif direction == "left":
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                     if direction == "root":
                        self = node.right
                     elif direction == "left":
                        parent.left = node.right
                     else:
                        parent.right = node.right
                print("after one or zero children removing ", node.value)
                self.display_aux(node)
                break

        return self
    def remove_value(self, value, node):
        """
        Recursive helper to remove node
        If the removal node has no children, simply remove the node.
        If the removal node has one children, update the child to be node.
        If the removal node has two children, then update the node with
        smallest node in the right child subtree.
        """
        if node is None:
            return

        if value < node.value:
            node.left = self.remove_value(value, node.left)
        elif value > node.value:
            node.right = self.remove_value(value, node.right)
        elif node.left is not None and node.right is not None:
            # Two children

            # Replace the current value by the smallest value of the right
            # subtree
            node.value = node.right.find_min_value()

            # Remove the smallest value of the right substree since its value
            # has been copied to the node to be removed.
            node.right = self.remove_value(node.value, node.right)
        else:
            # One or zero children
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node
    def find_min_value(self):
        if not self:
            return None

        current = self

        while current and current.left:
            current = current.left
        return current.value

    def display(self):
        lines, _, _, _ = self.display_aux(self)
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
