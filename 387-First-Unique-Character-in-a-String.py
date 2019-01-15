def firstUniqChar(s):
    counts = {}
    order = []

    for i in s:
        if i not in counts:
            counts[i] = 1
            order.append(i)
        else:
            counts[i] += 1

    for i in range(len(order)):
        if counts[order[i]] == 1:
            return i
    return -1


s = "dddccdbba"
print firstUniqChar(s)
