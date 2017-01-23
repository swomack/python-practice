

def is_anagram(s, t):
    s.sort()
    t.sort()

    return s == t


print(is_anagram([3,2,1,4],[1,2,3,4]))
print(is_anagram([3,2,1,5],[1,2,3,4]))
