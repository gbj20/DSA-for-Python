from math import sqrt

class Solution:
    def countFactors(self, n):
        result = []
        count = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                result.append(i)
                count += 1
                if n // i != i:  
                    result.append(n // i)
                    count += 1
        return count, sorted(result)


#custom input
n = int(input("Enter a number: "))
sol = Solution()
count, factors = sol.countFactors(n)

print(f"Number of factors of {n}: {count}")
print(f"Factors: {factors}")
