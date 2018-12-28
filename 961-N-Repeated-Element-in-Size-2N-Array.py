def repeatedNTimes(A):
    counts = {}
    for i in range(len(A)):
        if A[i] not in counts:
            counts[A[i]] = 1
        else:
            counts[A[i]] += 1

    for key, value in counts.items():
        if value == len(A) / 2:
            return key


A = [5, 1, 5, 2, 5, 3, 5, 4]
print repeatedNTimes(A)