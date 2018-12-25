import heapq

def findKthLargest(nums, k):

    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i] * -1)

    for j in range(k):
        result = heapq.heappop(heap)

    return result * -1

nums = [1, 24, 43, 4, 123, 12, 34, 5, 44]
k = 2
#Output: 5

print findKthLargest(nums, k)