# Ascending order
class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

sol = Solution()
print(sol.selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
