"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""

def isomorphic(s, t):
    if len(s) != len(t): return False
    
    hashA, hashB = {}, {}
    
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        
        if (c1 in hashA and hashA[c1] != c2 or
            c2 in hashB and hashB[c2] != c1): return False
        
        hashA[c1] = c2
        hashB[c2] = c1
    
    return True


print(isomorphic('egg', 'add'))
print(isomorphic('foo', 'bar'))