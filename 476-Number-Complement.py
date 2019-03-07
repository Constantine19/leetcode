def findComplement(num):
    compliment_bin = ""
    num_bin = bin(num).replace("0b", "")

    for bit in num_bin:
        if bit == "0":
            compliment_bin += "1"
        else:
            compliment_bin += "0"
    compliment_dec = int(compliment_bin, 2)

    return compliment_dec


num = 5
print findComplement(num)