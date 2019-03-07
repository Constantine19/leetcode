def hammingDistance(x, y):
    count = 0

    x_bin = bin(x).replace("0b", "").zfill(64)
    y_bin = bin(y).replace("0b", "").zfill(64)

    for i in range(64):
        if x_bin[i] != y_bin[i]:
            count += 1
    return count


x = 1
y = 4
print hammingDistance(x, y)
