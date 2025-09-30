# nums = [[5, "*", "*"], ["*", 6, "*"], ["*", "*", 9]]

# rows = len(nums)
# cols = len(nums[0])
# for i in range(0, rows):
#     for j in range(0, cols):
#         if j == i:
#             print(nums[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

nums = [["*", "*", 5], ["*", 6, "*"], [9, "*", "*"]]

rows = len(nums)
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i <= j or i > j:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
