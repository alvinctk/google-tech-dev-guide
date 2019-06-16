class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self)

def validateBst(tree):
    return validate_bst_helper(tree, True, [])

def validate_node(node, valid, insert_node):
    debug = False
    if not node:
        return True
    valid_left = lambda t: t.left.value < t.value
    valid_right = lambda t: t.value <= t.right.value
    valid_left_right = lambda t: t.left.value < t.right.value
    n = len(insert_node)
    i = n - 1
    current = node
    if debug: print("check insert node", insert_node)
    while i >= 0 and n >= 1:
        if debug: print("insert node", insert_node[i].value, "node.value", current.value)
        if insert_node[i].left is current:
            valid = valid and  (node.value < insert_node[i].value)
            if debug: print("check if {} < {} = {}".format(node.value, insert_node[i].value, valid))

        elif insert_node[i].right is current:
            valid = valid and (node.value >= insert_node[i].value)
            if debug: print("check if {} >= {} = {}".format(node.value, insert_node[i].value, valid))

        if not valid:
            if debug: print("stopping early", valid)
            return valid
        current = insert_node[i]
        i -= 1

    if node.left and node.right:
        valid = valid and valid_left(node) and valid_right(node) and valid_left_right(node)
    elif node.left:
        valid = valid and valid_left(node)
    elif node.right:
        valid = valid and valid_right(node)

    if debug: print("helper return valid = ", valid)
    return valid


def validate_bst_helper(node, valid, insert_node):
    debug = False
    if debug: print ("helper", node, valid, insert_node)
    if node is None:
        return valid
    valid = validate_node(node, valid, insert_node)
    if debug: print("valid", valid)
    if not valid:
        return valid
    v = validate_bst_helper

    insert_node.append(node)
    if node.left and node.right:
        valid = v(node.left, valid, insert_node) and v(node.right, valid, insert_node)
    elif node.left:
        valid = v(node.left, valid, insert_node)
    else:
        valid = v(node.right, valid, insert_node)
    del insert_node[-1]
    return valid

if __name__ == "__main__":
    # test6 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
    test6 = BST(10).insert(5).insert(5).insert(6)
    test6.left.right.right = BST(11)
    print("validate BST is ", validateBst(test6))


