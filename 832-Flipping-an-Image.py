def flipAndInvertImage(A):
    # Reverse
    for arr in A:
        arr.reverse()

        # Invert
        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    return A


A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print flipAndInvertImage(A)
