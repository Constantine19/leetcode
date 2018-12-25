def strStr(haystack, needle):
    if len(haystack) >= len(needle) and needle in haystack:
        if len(needle) > 0:
            return haystack.index(needle)
        else:
            return 0
    else:
        return -1

haystack = "aaaaa"
needle = "bba"
print strStr(haystack,needle)