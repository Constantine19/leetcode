def lengthOfLastWord(s):
    my_list = s.split()
    if len(my_list) <= 0:
        return 0
    else:
        return len(my_list[-1])


s = "Hellou j"
print lengthOfLastWord(s)
