"""
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""


def diStringMatch(S):
    low = 0
    high = len(S)
    result = []

    for i in range(len(S)):
        if S[i] == "I":
            result.append(low)
            low += 1
        elif S[i] == "D":
            result.append(high)
            high -= 1

    result.append(low)
    return result


S = "IDIDI"
print diStringMatch(S)
