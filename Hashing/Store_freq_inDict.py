nums = [2,3,3,3,4,4,5,5,6,6,6,7,7,7,7,65,4,4,3,3,32]
hash_map = {}
n = len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0)+1
print(hash_map)
