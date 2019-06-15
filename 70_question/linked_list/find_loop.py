# O(n) time | O(1) space
def find_loop(head):
    """
    Returns the node that originates a loop if a loop exists
    """
    if not head:
        return None

    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break
    if slow is fast:
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
    else:
        return None
