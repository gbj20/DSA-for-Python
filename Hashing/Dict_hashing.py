nums = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
hash_map = {}
n = len(nums)

# frequency map
for i in range(n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

for val in m:
    if val < 1 or val > 10:
        print(0)
    else:
        print(val, ":", hash_map.get(val, 0))
