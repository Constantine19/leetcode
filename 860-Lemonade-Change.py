def lemonadeChange(bills):
    reserve = {5: 0, 10: 0, 20: 0}
    for i in range(len(bills)):
        if bills[i] == 5:
            reserve[5] += 1
        elif bills[i] == 10:
            if reserve[5] > 0:
                reserve[5] -= 1
                reserve[10] += 1
            else:
                return False
        else:
            if reserve[10] > 0:
                if reserve[5] > 0:
                    reserve[10] -= 1
                    reserve[5] -= 1
                    reserve[20] += 1
                else:
                    return False
            else:
                if reserve[5] >= 3:
                    reserve[5] -= 3
                    reserve[20] += 1
                else:
                    return False
    return True


bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print lemonadeChange(bills)