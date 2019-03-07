def maxSubArray(nums):
    max_so_far, curr_sum = -2**31, 0
    for i in range(len(nums)):
        if curr_sum + nums[i] < 0:
            curr_sum, max_so_far = 0, max(max_so_far, curr_sum+nums[i])
        else:
            curr_sum, max_so_far = curr_sum + nums[i], max(max_so_far, curr_sum+nums[i])
    return max_so_far


"""
     max_so_far, curr_sum = -2**31, 0
        for i in range(len(nums)):
            if curr_sum+nums[i] < 0:
                curr_sum, max_so_far = 0, max(max_so_far, nums[i])
            else:
                curr_sum, max_so_far = curr_sum + nums[i], max(max_so_far, curr_sum + nums[i])
        return max_so_far
"""


"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maxSubArray(nums)