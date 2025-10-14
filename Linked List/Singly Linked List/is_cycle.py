from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


# Creating linked list: 3 -> 2 -> 0 -> -4
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

# last node points back to node with value 2
head.next.next.next.next = head.next

sol = Solution()
cycle_exists = sol.hasCycle(head)

print(cycle_exists)
