from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                # Handle collisions
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                if stack and stack[-1] == abs(a):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(a)
        return stack


obj = Solution()
print(obj.asteroidCollision([5, 10, -5]))
