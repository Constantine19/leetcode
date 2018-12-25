def isAnagram(s, t):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in alphabet:
        if s.count(i) == t.count(i):
            continue
        else:
            return False

    return True


s = "anagram"
t = "nagaram"
print isAnagram(t, s)
