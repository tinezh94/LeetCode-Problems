"""
    Given two strings, one is a subsequence if all of the elements of the first string occur in the same order within the second string. They 
    do not have to have to be contiguous in the second string, but order must be maintained. For example, given the string 'I like cheese',
    the words('I','cheese') are one possible subsequence of that string. Words are space delimited.
    
    Given two strings, s and t, where t is a subsequence of s, report the words of s, missing in t(case sensitive), in the order they are missing.
"""

def missingWords(s, t):
    res = []
    newS = s.split(' ')
    newT = t.split(' ')

    for i in range(len(newS)):
        if newS[i] not in newT:
            res.append(newS[i])
    
    return res


print(missingWords('I like cheese', 'like'))
print(missingWords('I like-cheese', 'cheese'))
print(missingWords('I like-cheese', 'like-cheese'))