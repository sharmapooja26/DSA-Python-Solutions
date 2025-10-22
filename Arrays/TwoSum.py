def twoSum(nums,target):
    hashMap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashMap:
            return [hashMap[diff],i]
        hashMap[num] = i
    return [] 

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))