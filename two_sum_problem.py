nums = [2,7,11,15]
target = 9
seen = {}
for i, nums in enumerate(nums):
    needed = target - nums
    if needed in seen:
        print(seen[needed],i)
    seen[nums] = i