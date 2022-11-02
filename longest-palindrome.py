"""

409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

"""

from collections import Counter

def longestPalindrome(s):
    count = Counter(s)
    length = 0
    
    for c in count.values():
        # print(c)
        length += c // 2 * 2
        # print(length)
        
        if length % 2 == 0 and c % 2 == 1:
            length += 1
    
    return length
    
print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("abcccccadddcd"))