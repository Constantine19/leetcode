def numJewelsInStones(J, S):
    result = []
    jewels, stones = list(J), list(S)

    for stone in stones:
        if stone in jewels:
            result.append(stone)
    return len(result)


J = "aA"
S = "aAAbbbb"
print numJewelsInStones(J, S)
