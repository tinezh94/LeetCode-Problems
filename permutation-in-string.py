"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

"""

def checkInclusion(s1, s2):
    hashA, hashB = {}, {}
    
    if len(s1) > len(s2): return False
    
    for char in s1:
        hashA[char] = hashA.get(char, 0) + 1

    for i in range(len(s1)):
        hashB[s2[i]] = hashB.get(s2[i], 0) + 1
    
    # print(hashA)
    # print(hashB)
    
    if hashA == hashB:
        return True
    
    l = 0
    
    for i in range(len(s1), len(s2)):
        # print(range(len(s1), len(s2)))
        char = s2[i]
        hashB[char] = hashB.get(char, 0) + 1
        # print('.....', hashB)
        hashB[s2[l]] -= 1
        # print('...', hashB)
        if hashB[s2[l]] == 0:
            del hashB[s2[l]]
        l += 1
        # print('---', hashA)
        # print('...--', hashB)
        if hashA == hashB:
            return True
        
    return False

        

# print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab","eidboaoo"))