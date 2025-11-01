class Solution:
    def isBalanced(self, root):
        self.diameter = 0
        return self.Solve(root) != -1   # Returns True if tree is balanced

    def Solve(self, node):
        if node is None:
            return 0

        leftHeight = self.Solve(node.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.Solve(node.right)
        if rightHeight == -1:
            return -1

        # If difference in height > 1, it's not balanced
        if abs(leftHeight - rightHeight) > 1:
            return -1

        # Optional: update diameter (not necessary for balance check)
        self.diameter = max(self.diameter, leftHeight + rightHeight)

        # Return height of current node
        return 1 + max(leftHeight, rightHeight)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create a sample tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

obj = Solution()
print(obj.isBalanced(root))  # Output: True
