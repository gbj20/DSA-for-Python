def upperBound(arr, x, n) -> int:
    n = len(arr)
    upper_bound = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            upper_bound = mid
            high = mid - 1
        else:
            low = mid + 1

    print(upper_bound)


pass

arr = [1, 3, 5, 7, 9]
upperBound(arr, 5, len(arr))

x = 6
upperBound(arr, 6, len(arr))

x = 9
upperBound(arr, 9, len(arr))  # return n
