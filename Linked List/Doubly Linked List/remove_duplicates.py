# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    # Function to remove duplicates from an unsorted doubly linked list
    def removeDuplicates(self, head):
        if not head:
            return None

        seen = set()   # store values we’ve already seen
        curr = head

        while curr:
            if curr.data in seen:
                # Remove the duplicate node
                if curr.next:
                    curr.next.prev = curr.prev
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    # if duplicate was at head
                    head = curr.next
            else:
                seen.add(curr.data)
            curr = curr.next
        return head


# Helper function to print the list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.next else "\n")
        temp = temp.next


# Example
head = Node(4)
node2 = Node(3)
node3 = Node(4)
node4 = Node(2)
node5 = Node(3)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

print("Original list:")
print_list(head)

sol = Solution()
new_head = sol.removeDuplicates(head)

print("\nAfter removing duplicates:")
print_list(new_head)
