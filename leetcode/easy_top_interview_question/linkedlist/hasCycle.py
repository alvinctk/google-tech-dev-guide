# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if head and not head.next:
            return False

        fast = slow = head
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        return slow is fast
