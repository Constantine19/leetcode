class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left_index = 0
        right_index = len(s)-1
        s = s.lower()

        while left_index < right_index:
            leftChar = s[left_index]
            rightChar = s[right_index]

            if (leftChar < "a" or leftChar > "z") and not leftChar.isdigit():
                left_index += 1
            elif (rightChar < "a" or rightChar > "z") and not rightChar.isdigit():
                right_index -= 1

            elif rightChar == leftChar:
                left_index += 1
                right_index -= 1
            else:
                return False
        return True