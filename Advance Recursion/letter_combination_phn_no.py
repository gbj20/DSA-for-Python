from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []  # Empty input → no combinations

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            # Base case: if combination is complete
            if index == len(digits):
                result.append("".join(path))
                return

            # Get the letters for the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # backtrack

        backtrack(0, [])
        return result


obj = Solution()
print(obj.letterCombinations("23"))
