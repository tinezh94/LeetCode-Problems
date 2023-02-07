"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


def firstUniqChar(s):
    hash = {}
    for char in s:
        hash[char] = hash.get(char, 0) + 1
    # print(hash)
    for key in hash:
        if hash[key] == 1:
            return s.index(key)
    return -1
    

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))

