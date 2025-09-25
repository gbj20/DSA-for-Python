
##Brute force solution
# a = [100,99,50,5,333]

# sorted = a.sort()
# print(a[-2])


##better solution without sorting

arr = [88,52,63,48,96]
largest = float('-inf')
sec_largest = float('-inf')

n  = len(arr)
for i in range(0,n):
    largest = max(largest,arr[i])
for i in range(0,n):
    if arr[i]>sec_largest and arr[i]!=largest:
        sec_largest = arr[i]
print(sec_largest)