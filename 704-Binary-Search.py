"""
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
"""

def search(nums, target):
    lower_index = 0
    upper_index = len(nums)-1

    while lower_index < upper_index:
        midpoint = int((lower_index + upper_index)/2)
        #print("midpoint: ", midpoint)
        if nums[midpoint] < target:
            lower_index += 1
        elif nums[midpoint] > target:
            upper_index -= 1
        else:
            return midpoint
    return False

nums = [5]
target = 5

print (search(nums, target))