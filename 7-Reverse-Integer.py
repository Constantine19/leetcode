class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2 ** 31 > x > 2 ** 31:
            return 0

        reversed = str(x)[::-1]

        if reversed[0] == '0':
            reversed = reversed[1::]
        if reversed[-1] == '-':
            return int('-' + reversed[:-1])

        else:
            return int(reversed)