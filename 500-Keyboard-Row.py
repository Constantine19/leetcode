def findWords(words):
    first_row = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    second_row = {'a', 's', 'd',  'f', 'g',  'h', 'j', 'k', 'l'}
    third_row = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

    keyboard = [first_row, second_row, third_row]

    valid_words = []

    for word in words:
        word_set = set(word.lower())
        for row in keyboard:
            if word_set.issubset(row):
                valid_words.append(word)
                break

    return valid_words


words = ["Hello", "Alaska", "Dad", "Peace"]
print findWords(words)
