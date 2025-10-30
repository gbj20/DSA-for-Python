from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # Base case: valid combination formed
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' if it won’t break validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


obj = Solution()
print(obj.generateParenthesis(3))
