class Solution:
    def findPlatform(self, arr, dep):
        n = len(arr)
        arr.sort()
        dep.sort()

        plat_needed = 1
        result = 1
        i = 1
        j = 0

        while i < n and j < n:
            # If next train arrives before the previous one departs
            if arr[i] <= dep[j]:
                plat_needed += 1
                i += 1
            else:
                plat_needed -= 1
                j += 1

            result = max(result, plat_needed)

        return result


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(Solution().findPlatform(arr, dep))
