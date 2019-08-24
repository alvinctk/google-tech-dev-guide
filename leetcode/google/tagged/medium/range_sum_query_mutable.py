from typing import List
"""
Problem: https://leetcode.com/problems/range-sum-query-mutable

Complexity Analysis using Segment Trees

Time complexity: O(n), because number of nodes in each level is half the number in the level below.

So if we sum the number by level we will get:
n + n/2 + n/4 + n/8 + ... + 1 (approximately equal =) 2n

Space complexity: O(n)
We used 2n extra space to store the segment tree.
Also, recursive function is used. The recursive stack depth is O(log n) since the pivot chosen makes the tree balanced.

However, the space complexity is dominated by the 2n.
"""

class SegmentNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        def create_segment_tree(nums, left, right):
            if left > right:
                # base case
                return None

            elif left == right:
                # leaf node
                node = SegmentNode(left, right)
                node.sum = nums[left]
                return node

            mid = left + (right - left)//2
            root = SegmentNode(left, right)

            # recursively build the segment tree
            root.left = create_segment_tree(nums, left, mid)
            root.right = create_segment_tree(nums, mid + 1, right)

            # Store total sum
            root.sum = root.left.sum + root.right.sum

            return root

        self.root = create_segment_tree(nums, 0, len(nums)-1)




    def update(self, i: int, val: int) -> None:
        def helper(node, i, val):
            # update at leaf node
            if node.start == node.end:
                node.sum = val
                return node.sum

            mid = node.start + (node.end - node.start)//2
            if i <= mid:
                node.left.sum = helper(node.left, i, val)
            else:
                node.right.sum = helper(node.right, i, val)

            # Propogate the changes back to root/node
            node.sum = node.left.sum + node.right.sum
            return node.sum
        return helper(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def helper(node, i, j):
            if node.start == i and node.end == j:
                return node.sum
            mid = node.start + (node.end - node.start)//2
            if j <= mid:
                return helper(node.left, i, j)
            elif i > mid:
                return helper(node.right, i, j)
            else:
                # By inverting if-statement, we have j > mid and i<= mid
                # Then the range is i <= mid < j
                return helper(node.left, i, mid) + helper(node.right, mid + 1, j)
        return helper(self.root, i, j)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
