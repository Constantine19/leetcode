def lengthOfLongestSubstring(s):
    counts = {}
    ans = ""

    if not s:
        return 0
    i = 0
    while i < (len(s)):
        if s[i] not in ans:
            ans += str(s[i])
            if i == len(s) - 1:
                counts[ans] = len(ans)
        else:
            counts[ans] = len(ans)
            i = i - len(ans)
            ans = ""
        i += 1
    print ans
    print counts
    return len(max(counts, key=counts.get))


s = "dvdf"
print lengthOfLongestSubstring(s)
