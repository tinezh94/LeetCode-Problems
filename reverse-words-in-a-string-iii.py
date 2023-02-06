"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""


def reverseWords(s):
    s = s.split()
    res = []
    for i in range(len(s)):
        word = s[i]
        word = word[::-1]
        res.append(word)
    
    return " ".join(res)
    
    
print(reverseWords("Let's take LeetCode contest"))
# print(reverseWords("God Ding"))