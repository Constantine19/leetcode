def plusOne(digits):
    for i in range(len(digits)):
        digits[i] = str(digits[i])
    number = ''.join(digits)
    answer = int(number) + 1
    answer_list = list(str(answer))
    for i in range(len(answer_list)):
        answer_list[i] = int(answer_list[i])
    return answer_list


digits = [1, 2, 3]
print plusOne(digits)