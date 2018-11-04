class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        counts = {}
        my_list = []

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
                my_list.append(i)

        if val in my_list:
            my_list.remove(val)

        return len(my_list)
