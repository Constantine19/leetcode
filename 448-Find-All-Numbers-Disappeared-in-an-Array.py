def findDisappearedNumbers(nums):
    result = []
    low, high = 1, len(nums)
    nums_set = set(nums)

    if not nums_set:
        return result
    for i in range(low, high + 1):
        if i not in nums_set:
            result.append(i)
    return result


nums = [1, 1]
print findDisappearedNumbers(nums)
