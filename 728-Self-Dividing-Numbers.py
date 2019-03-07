"""
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
"""


def selfDividingNumbers(left, right):
    def self_dividing(value):
        for digit in value:
            if digit == '0' or int(value) % int(digit) > 0:
                return False
            else:
                continue
        return True

    result = []
    for value in range(left, right + 1):
        if self_dividing(str(value)):
            result.append(value)
    return result


left = 1
right = 22
print selfDividingNumbers(left, right)
