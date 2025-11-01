class Solution:
    def maxPathSum(self, root):
        self.maxi = float('-inf')
        self.solve(root)
        return self.maxi

    def solve(self, node):
        if node is None:
            return 0

        # Compute left and right subtree sums
        left_sum = self.solve(node.left)
        right_sum = self.solve(node.right)

        # Ignore negative sums (we don’t want to include bad paths)
        left_sum = max(left_sum, 0)
        right_sum = max(right_sum, 0)

        # Update the global maximum path sum
        self.maxi = max(self.maxi, left_sum + right_sum + node.val)

        # Return max gain if we continue the path upward
        return node.val + max(left_sum, right_sum)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create a sample tree
root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

obj = Solution()
print(obj.maxPathSum(root))
