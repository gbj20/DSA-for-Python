class Solution:
    def merge_array(self, left, right):
        result = []
        i, j = 0, 0
        n, m = len(left), len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < n:
            result.append(left[i])
            i += 1
        while j < m:
            result.append(right[j])
            j += 1

        return result

    def mergeSort(self, arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left_arr = self.mergeSort(arr[:mid])
        right_arr = self.mergeSort(arr[mid:])

        return self.merge_array(left_arr, right_arr)


sol = Solution()
arr = [4, 1, 3, 9, 7]
print(sol.mergeSort(arr))

arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sol.mergeSort(arr2))
