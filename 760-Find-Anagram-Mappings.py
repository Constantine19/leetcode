def anagramMappings(A, B):
    result = []
    for i in range(len(A)):
        if A[i] in B:
            result.append(B.index(A[i]))
    return result


A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
# [1, 4, 3, 2, 0]
print anagramMappings(A, B)
