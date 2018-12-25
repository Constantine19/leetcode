
def majorityElement(nums):
    counts = {}
    for i in range(len(nums)):
        if nums[i] in counts:
            counts[nums[i]] += 1
        else:
            counts[nums[i]] = 1

    for i in counts:
        if counts[i] == max(counts.values()):
            return i

nums = [2,2,1,1,1,2,2,8,8,8,8,8,8,8,8,8]