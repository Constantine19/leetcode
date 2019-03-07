def longestOnes(a):
    count = 0
    result = []

    for i in range(len(a)):
        if a[i] == 1:
            count += 1
        else:
            result.append(count)
            count = 0

    return max(result)


a = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# K = 2
print longestOnes(a)
