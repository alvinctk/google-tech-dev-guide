
Let A be the node that must be rebalanced
There are four unique cases of A:
- Case 1: An insertion onto left subtree of the left child of A
- Case 2: An insertion onto right subtree of the left child of A
- Case 3: An insertion onto left subtree of the right child of A
- Case 4: An insertion onto right subtree of the right child of A

Case 1 and case 4 are classified as outside case. In order to fix the outside
case, a single rotation is required.

### Case 1 requires a right rotation.
```
          k2             Right          k1
          / \            Rotation     /   \  
        k1   Z           ---->            k2
        /\                          /     /\
       /  Y                        x     Y  Z
      x
```
```python
def rotate_with_left_child(self, k2: Node):
    k1 = k2.left        # keep a reference to k1
    k2.left = k1.right  # k2.left assigned to Y
    k1.right = k2       
    k2.height = max(height(k2.left) + height(k2.right)) + 1 
    k1.height = max(height(k1.left) + height(k1.right)) + 1
    return k1
```
### Case 4 requires a left rotation. 
```
          k2             Left           k1
          / \            Rotation      /   \  
        Z    k1           ---->      k2     
             /\                      /\      \
            Y  \                    Z  Y      X  
                X
```

```python
def rotate_with_right_child(self, k2: Node):
    k1 = k2.right         # Keep a reference to k1
    k2.right = k1.left    # k2.right = Y, to remove k1.left
    k1.left = k2
    k2.height = max(height(k2.left) + height(k2.right)) + 1 
    k1.height = max(height(k1.left) + height(k1.right)) + 1
    return k1
```
## Case 2 and 3 are classified as inside case.
In order to fix the inside case, a double rotation is required.

### Case 2: An insertion onto right substree of the left child of k3
To fix case 2: Left-right rotation => Double rotation
Double rotate binary tree node: first left child with its right child;
then node k3 with new left child.
```
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
```
```python
def double_with_left_child(self, k3: Node):
    # To left rotate on k1 = k3.left node
    k3.left = self.rotate_with_right_child(k3.left)
    # To right rotate on k3 node
    return self.rotate_with_left_child(k3)
```

### Case 3, requires a Right-Left rotation, is similar to case 2. 
```python
def double_with_left_child(self, k3: Node):
    # To right rotate on k1 = k3.right node
    k3.right = self.rotate_with_left_child(k3.right)
    # To left rotate on k3 node
    return self.rotate_with_right_child(k3)
```
