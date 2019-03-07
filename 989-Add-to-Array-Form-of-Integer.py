def addToArrayForm(A, K):
    a = ""
    for i in A:
        a += str(i)
    my_list = map(int, list(str(int(a) + K)))

    return my_list


A = [1, 2, 0, 0]
K = 34

print addToArrayForm(A, K)
