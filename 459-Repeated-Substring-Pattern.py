def repeatedSubstringPattern(s):
    # counts = {}
    # if len(s) > 1:
    #     for i in range(len(s)):
    #         if s[i] in counts:
    #             counts[s[i]] += 1
    #         else:
    #             counts[s[i]] = 1
    #     ordered_values = counts.values()
    #
    #     if ordered_values.count(ordered_values[0]) == len(ordered_values):
    #         return True
    #     else:
    #         return False
    # return False

    if len(s) > 1:
        for i in range(len(s)):
            swapped = s[::-1]
            if swapp

s = 'abcabcabcabcbac'
print repeatedSubstringPattern(s)