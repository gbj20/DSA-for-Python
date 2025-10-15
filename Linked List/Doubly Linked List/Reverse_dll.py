
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverse(self, head):
        if head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.next else "\n")
        temp = temp.next


# Create doubly linked list: 1 <-> 2 <-> 3 <-> 4
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

print("Original list:")
print_list(head)

# Reverse the doubly linked list
sol = Solution()
reversed_head = sol.reverse(head)

print("\nReversed list:")
print_list(reversed_head)
