def isMonotonic(A):
    increasing = False
    decreasing = False

    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            decreasing = True
        elif A[i] > A[i + 1]:
            increasing = False

    return increasing or decreasing

A = [1, 2, 2, 3, 4]
print isMonotonic(A)
