def twoSum(nums, target):
    compliments = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in compliments:
            return i, compliments[compliment]
        else:
            compliments[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print twoSum(nums, target)