def findTheDifference(s, t):
    s_set = set(s)
    t_set = set(t)
    result = ""

    for i in t_set - s_set:
        result += i

    return result


s = "abcd"
t = "abcde"
print findTheDifference(s, t)
