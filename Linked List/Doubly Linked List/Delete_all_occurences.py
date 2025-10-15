# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    # Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        if not head.next and head.data == x:
            return None
        temp = head
        previous = None
        new_head = head

        while temp is not None:
            if temp.data == x:
                if previous:
                    previous.next = temp.next
                if temp.next:
                    temp.next.prev = previous
                if temp == new_head:
                    new_head = new_head.next
            previous = temp
            temp = temp.next
        return new_head


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.next else "\n")
        temp = temp.next


head = Node(2)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)

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
reversed_head = sol.deleteAllOccurOfX(head, 2)
print_list(reversed_head)
