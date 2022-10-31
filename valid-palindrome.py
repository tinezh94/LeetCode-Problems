"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

# def validPalindrome(s):
#     newS = ''
#     for char in s:
#         if char.isalnum():
#             newS += char.lower()
#     return True if newS == newS[::-1] else False

def isAlphaNum(char):
    return (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))

def validPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not isAlphaNum(s[l]):
            l += 1
        while l < r and not isAlphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
            
        l += 1
        r -= 1
    return True



print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))
print(validPalindrome(" "))

