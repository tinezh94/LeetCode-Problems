"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""

def validAnagram(s, t):
    if len(s) != len(t):
         return False

    hashMapS = {}
    hashMapT = {}

    for i in range(len(s)):
        hashMapS[s[i]] = hashMapS.get(s[i], 0) + 1
        hashMapT[t[i]] = hashMapT.get(t[i], 0) + 1
    
    for key in hashMapS:
        if hashMapS[key] != hashMapT.get(key, 0):
            return False
    
    return True




print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "car"))