def reverseStr(s, k):
    s_split = []
    for i in range(0, len(s), k):
        s_split.append(s[i:i + k])

    for i in range(len(s_split)):
        if i % 2 == 0:
            s_split[i] = s_split[i][::-1]
    return ''.join(s_split)


s = "abcdefg"
k = 2
print reverseStr(s, k)