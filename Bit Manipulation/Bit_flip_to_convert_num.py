class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_value = start ^ goal      # XOR highlights different bits
        return bin(xor_value).count('1')  # Count number of 1s


obj = Solution()
print(obj.minBitFlips(10, 7))  # Output: 3
