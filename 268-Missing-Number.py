def missingNumber(nums):
    n = len(nums) # 5
    return n * (n+1) / 2 - sum(nums)


nums = [0, 1, 2, 4, 5]
print missingNumber(nums)
