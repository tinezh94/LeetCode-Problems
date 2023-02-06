"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

"""

def reverseString(s):
    l, r = 0, len(s) - 1
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s
    

print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))