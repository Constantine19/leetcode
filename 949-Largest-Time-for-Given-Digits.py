from itertools import permutations

def largestTimeFromDigits(A):
    init = (-1, -1, -1, -1)
    result = [init]

    for p in permutations(A):
        if (p[0] <= 1 or (p[0] == 2 and p[1] <= 3)) and p[2] < 6:
            if result[0] < p:
                result[0] = p
        if result[0] == init:
            return ''
    result = result[0]
    return '{}{}:{}{}'.format(result[0], result[1], result[2], result[3])


A = [1, 2, 3, 4]
print largestTimeFromDigits(A)
