def twoSum(numbers, target):
    compliments = {}
    for i in range(len(numbers)):
        compliment = target - numbers[i]
        if compliment in compliments:
            return sorted([i+1, compliments[compliment]+1])
        else:
            compliments[numbers[i]] = i
    return False


numbers = [2, 7, 11, 15]
target = 9
print twoSum(numbers, target)
