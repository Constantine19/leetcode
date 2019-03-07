def isIsomorphic(s, t):
    counts_s, counts_t = {}, {}
    values_s, values_t = [], []

    # if set(s) == set(t):
    #     return False

    if not s and not t:
        return True

    for i in range(len(s)):
        if s[i] not in counts_s:
            counts_s[s[i]] = 1
        else:
            counts_s[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in counts_t:
            counts_t[t[i]] = 1
        else:
            counts_t[t[i]] += 1

    for value in counts_s.values():
        values_s.append(value)

    for value in counts_t.values():
        values_t.append(value)

    return set(values_s) == set(values_t)


s = "a"
t = "a"
print isIsomorphic(s, t)
