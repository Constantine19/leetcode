def mostCommonWord(paragraph, banned):
    #words = paragraph.replace(',', '').replace('.', '').replace("!", "").lower().split()
    counts = {}

    for i in paragraph.split(','):
        print i



    # for i in range(len(words)):
    #     if words[i] not in counts:
    #         counts[words[i]] = 1
    #     else:
    #         counts[words[i]] += 1
    #
    # for key in counts.keys():
    #     if key in banned:
    #         del counts[key]
    #
    # return (max(counts, key=counts.get))


paragraph = "a, a, a, a, b, b, b, c, c"
banned = ["a"]

print mostCommonWord(paragraph, banned)
