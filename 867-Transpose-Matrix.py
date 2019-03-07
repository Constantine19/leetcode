from numpy import zeros


def transpose(A):
    result = []
    for i in range(len(A)):
        chunk = []
        for j in range(len(A)):
            chunk.append(A[j][i])
        result.append(chunk)

    return result


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print transpose(A)
