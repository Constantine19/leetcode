def strWithout3a3b(A, B):
    if A == 0:
        return "b" * B
    elif B == 0:
        return "a" * A
    elif A == B:
        return "ab" * A
    elif A > B:
        return "aab" + strWithout3a3b(A - 2, B - 1)
    else:
        return "bba" + strWithout3a3b(A - 1, B - 2)


A = 5
B = 6
print strWithout3a3b(A, B)
