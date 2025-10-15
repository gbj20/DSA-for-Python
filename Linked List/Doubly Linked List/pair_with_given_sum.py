from typing import List, Optional


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional["Node"]) -> List[List[int]]:
        left = head
        right = head
        ans = []

        # Move right to the end
        while right.next:
            right = right.next

        # Two-pointer approach
        while left is not None and right is not None and left.data < right.data:
            total = left.data + right.data

            if total == target:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif total > target:
                right = right.prev
            else:
                left = left.next
        return ans


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

# Find pairs with sum = 5
sol = Solution()
pairs = sol.findPairsWithGivenSum(5, head)

print("\nPairs with sum 5:")
print(pairs)
