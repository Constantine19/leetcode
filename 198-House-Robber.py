def rob(nums):
    even, odd = [], []
    for i in range(len(nums)):
        if i % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    print max(sum(even), sum(odd))



nums = [2, 7, 9, 3, 1]
print rob(nums)

"""
[2, 1, 1, 1, 1, 1, 1, 5]
"""
