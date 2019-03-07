def isNStraightHand(hand, W):
    return len(hand) % W == 0


hand = [1, 2, 3, 4, 5]
W = 4
print isNStraightHand(hand, W)
