class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Found a loop, now count its length
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Create a cycle: Node 5 -> Node 3
head.next.next.next.next.next = head.next.next

sol = Solution()
print("Length of loop:", sol.lengthOfLoop(head))
