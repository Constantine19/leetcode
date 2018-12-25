def detectCapitalUse(word):
    if word.isupper() or word.islower():
        return True
    else:
        if word[0].isupper() and word[1:].islower():
            return True
        else:
            return False

word = 'Usa'
print detectCapitalUse(word)