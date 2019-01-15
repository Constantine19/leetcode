def fib_rec(N):
    if N <= 1:
        return N
    else:
        return fib_rec(N - 2) + fib_rec(N - 1)


def fib_memo(N):
    lookup = {}
    if N in lookup:
        return lookup[N]

    result = fib_rec(N - 2) + fib_rec(N - 1)
    lookup[N] = result
    return result


N = 30
# print fib_rec(N)
print fib_memo(N)
