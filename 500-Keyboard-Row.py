def findWords(words):
    first_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    second_row = ['a', 's', 'd',  'f', 'g',  'h', 'j', 'k', 'l']
    third_row = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    print first_row
    print second_row
    print third_row

    counts = {}
    for word in words:
        for letter in word:
            if letter not in counts:
                counts[letter] = 1
        print i

    print words




words = ["Hello", "Alaska", "Dad", "Peace"]
findWords(words)
