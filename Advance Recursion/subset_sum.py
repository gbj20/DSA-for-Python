from typing import List


def isSubsetPresent(n: int, k: int, a: List[int]) -> bool:

    dp = [False] * (k + 1)
    dp[0] = True

    for num in a:

        for target in range(k, num - 1, -1):
            if dp[target - num]:
                dp[target] = True

    return dp[k]


print(isSubsetPresent(3, 5, [1, 2, 3]))
print(isSubsetPresent(4, 11, [2, 3, 7, 8]))
print(isSubsetPresent(3, 9, [1, 2, 3]))
