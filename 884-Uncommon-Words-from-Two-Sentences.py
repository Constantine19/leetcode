def uncommonFromSentences(A, B):
    A_list = A.split()
    B_list = B.split()

    combined_words = A_list + B_list

    uncommon = []
    counts = {}

    for i in range(len(combined_words)):
        if combined_words[i] not in counts:
            counts[combined_words[i]] = 1
        else:
            counts[combined_words[i]] += 1

    for key, value in counts.items():
        if value == 1 and key not in A_list:
            uncommon.append(key)
        elif value == 1 and key not in B_list:
            uncommon.append(key)

    return uncommon


A = "apple apple"
B = "banana"
print uncommonFromSentences(A, B)
