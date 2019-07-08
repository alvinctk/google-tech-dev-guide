from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        array = []
        q = deque()
        q.append(root)

        while q:
            # Breadth First Search to add all child node on this level

            node = q.popleft()
            value = str(node.val) if node else "None"
            array.append(value)
            if node:
                q.append(node.left)
                q.append(node.right)

        return ",".join(array)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if data[0] == "None":
            return None

        n = len(data)

        i = 0
        while i < n:
            if data[i] != "None":
                data[i] = TreeNode(int(data[i]))
            else:
                data[i] = None
            i += 1

        parent = 0
        last_child = 0

        while parent < n:
            # Traverse until parent is not None
            while parent < n and data[parent] == None:
                parent += 1

            # Out of bounds check
            if parent >= n:
                break
            left, right = last_child + 1, last_child + 2

            # Assign left, right to parent
            data[parent].left = data[left] if left < n else None
            data[parent].right = data[right] if right < n else None

            parent += 1
            last_child += 2

        # Returns root of binary tree
        return data[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
