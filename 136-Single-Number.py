class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        for i in counts:
            if counts[i] == 1:
                return i

        return False