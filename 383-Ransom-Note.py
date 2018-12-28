def canConstruct(ransomNote, magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    for i in range(len(ransomNote)):
        if ransomNote[i] not in magazine:
            return False
        else:
            magazine.remove(ransomNote[i])
    return True


print canConstruct("aa", "ab")
