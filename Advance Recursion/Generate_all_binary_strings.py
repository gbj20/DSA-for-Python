class Solution:
    def solve(self, index, numbers, result):
        # Base case
        if index == len(numbers):
            result.append("".join(numbers))
            return

        # Place '0'
        numbers[index] = "0"
        self.solve(index + 1, numbers, result)

        # Place '1'
        numbers[index] = "1"
        self.solve(index + 1, numbers, result)

    def binstr(self, n):
        numbers = ["0"] * n
        result = []
        self.solve(0, numbers, result)
        return result


obj = Solution()
print(obj.binstr(3))
