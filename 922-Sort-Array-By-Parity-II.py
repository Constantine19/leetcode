def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    odd = 1
    even = 0
    combined = []

    for i in range(len(A)):
        combined.append(0)

    for i in range(len(A)):
        if A[i] % 2 == 0:
            combined[even] = A[i]
            even += 2
        else:
            combined[odd] = A[i]
            odd += 2
    return combined

A = [4, 2, 5, 7]
print sortArrayByParityII(A)