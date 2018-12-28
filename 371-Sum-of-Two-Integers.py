def getSum(a, b):
    carry = 0
    sum_add = 0

    while carry != 0:
        if b == '0':
            return a
        elif a == '0':
            return b
        else:
            sum_add = a ^ b
            carry = (a & b) << 1

    return sum_add


a = 2
b = 4
print getSum(a, b)
