import collections

def largeGroupPositions(S):
    count = collections.Counter(S)

    return type(count)

S = "abbxxxxzzy"
# [[3,6]]
print largeGroupPositions(S)