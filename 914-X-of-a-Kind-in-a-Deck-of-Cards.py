def hasGroupsSizeX(deck):
    counts = {}

    for i in range(len(deck)):
        if deck[i] in counts:
            counts[deck[i]] += 1
        else:
            counts[deck[i]] = 1

    ordered_values = counts.values()
    if ordered_values.count(ordered_values[0]) == len(ordered_values):
        return True
    else:
        return False



deck = [1,2,3,5]
print hasGroupsSizeX(deck)