def sort_by_parity(A):
    even = []
    odd = []

    for i in range(len(A)):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
    return even + odd

A = [3, 1, 2, 4]
print sort_by_parity(A)