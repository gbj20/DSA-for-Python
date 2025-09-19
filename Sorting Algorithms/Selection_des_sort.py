class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] > arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

sol = Solution()
print(sol.selectionSort([1,2,3,4,5,6,7]))