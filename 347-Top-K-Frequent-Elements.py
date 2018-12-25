import heapq

def topKFrequent(nums, k):
    counts = {}
    for i in range(len(nums)):
        if nums[i] not in counts:
            counts[nums[i]] = 1
        else:
            counts[nums[i]] += 1

    print counts

    heap = []





    sorted_values = counts.values()
    sorted_values.sort(reverse=True)

    result = []
    for i in range(k):
        result.append(counts.keys()[counts.values().index(sorted_values[i])])

    return result


nums = [1, 2, 2, 2, 4, 5, 2, 2, 1, 1, 2, 3, 1]
k = 2

print topKFrequent(nums, k)
