# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        def print_nodes(node):
            current = node
            while current:
                print(current.val, end="")
                if current.next:
                    print(" -> ", end="")
                else:
                    print("", end="\n")
                current = current.next

        def helper(node):
            if node and node.next:
                last = node.next.next
                last = helper(node.next.next)
                # Store a reference to current node
                prev = node

                # Swap the pairs
                node = node.next
                node.next = prev

                # The remaining nodes after pairs
                node.next.next = last

            return node

        print("before swap:", end=" ")
        print_nodes(head)

        head = helper(head)

        print("after swap:", end=" ")
        print_nodes(head)
        return head


if __name__ == "__main__":
    x = ListNode(1)
    x.next = ListNode(2)
    x.next.next = ListNode(3)
    x.next.next.next = ListNode(4)
    y = Solution()
    y.swapPairs(x)


