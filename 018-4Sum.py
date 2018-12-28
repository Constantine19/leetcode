def fourSum(nums, target):
    for i in range(len(nums)):
        compliment = target - nums[i]
        print compliment


nums = [1, 0, -1, 0, -2, 2]
target = 0
"""
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

fourSum(nums, target)
