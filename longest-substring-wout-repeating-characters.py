"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def longestSubstring(s):
    char = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in char:
            char.remove(s[l])
            print('l', s[l])
            l += 1
        char.add(s[r])
        print('r', s[r])
        res = max(res, r - l + 1)
    return res


print(longestSubstring("abcabcbb"))
# print(longestSubstring("bbbbb"))
# print(longestSubstring("pwwkew"))