class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            nums = self.partition(arr, low, high)
            self.quickSort(arr, low, nums - 1)
            self.quickSort(arr, nums + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]   # last element as pivot
        i = low - 1         # place for smaller element

        for j in range(low, high):
            if arr[j] >= pivot:   # if element smaller than pivot
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


arr = [10, 7, 8, 99, 1, 5]
sol = Solution()
sol.quickSort(arr, 0, len(arr) - 1)
print(arr)
