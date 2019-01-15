def findMaxConsecutiveOnes(nums):
    count = 0
    lookup = []

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            lookup.append(count)
            count = 0
        lookup.append(count)
    return max(lookup)


nums = [1, 1, 0, 1, 1, 1]
print findMaxConsecutiveOnes(nums)
