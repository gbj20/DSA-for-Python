def getFloorAndCeil(a, n, x):
    n = len(a)
    floor = -1
    ceil = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return (a[mid], a[mid])
        elif a[mid] > x:
            ceil = a[mid]
            high = mid - 1
        else:
            floor = a[mid]
            low = mid + 1

    return [floor, ceil]


a = [10, 20, 30, 40, 50, 60]

print(getFloorAndCeil(a, len(a), 30))  # (30, 30)
print(getFloorAndCeil(a, len(a), 25))  # (20, 30)
print(getFloorAndCeil(a, len(a), 10))  # (10, 10)
print(getFloorAndCeil(a, len(a), 5))   # (-1, 10)
print(getFloorAndCeil(a, len(a), 65))  # (60, -1)
