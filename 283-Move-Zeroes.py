def moveZeros(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    print nums

    while count < len(nums):
        nums[count] = 0
        count += 1

    print nums

nums = [0,1,0,3,12]
moveZeros(nums)

"""
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""