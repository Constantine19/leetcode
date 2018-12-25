def isAnagram(s, t):
    for i in s:
        if s.count(i) != t.count(i):
            return False
        else:
            return True


s = "anagram"
t = "nagaram"
print isAnagram(t, s)
