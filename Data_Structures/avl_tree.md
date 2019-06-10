
Let A be the node that must be rebalanced
There are four unique cases of A:
- Case 1: An insertion onto left subtree of the left child of A
- Case 2: An insertion onto right subtree of the left child of A
- Case 3: An insertion onto left subtree of the right child of A
- Case 4: An insertion onto right subtree of the right child of A

Case 1 and case 4 are classified as outside case. In order to fix the outside
case, a single rotation is required.

Case 1 requires a right rotation. Abstractly,
```
          k2             Right          k1
          / \            Rotation     /   \  
        k1   Z           ---->            k2
        /\                          /     /\
       /  Y                        x     Y  Z
      x
```
```python
# Case 1: Rotate with left child (or single right rotation)

k1 = k2.left        # keep a reference to k1
k2.left = k1.right  # k2.left assigned to Y
k1.right = k2       
k2.height = max(height(k2.left) + height(k2.right)) + 1 
k1.height = max(height(k1.left) + height(k1.right)) + 1
```
Case 4 requires a left rotation. Abstractly, 
```
          k2             Left           k1
          / \            Rotation      /   \  
        Z    k1           ---->      k2     
             /\                      /\      \
            Y  \                    Z  Y      X  
                X
```

Case 2 and 3 are classified as inside case. In order to fix the inside case, a
double rotation is required.


