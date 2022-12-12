"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def isPalindrome(x):
    x = str(x)
    l, r = 0, len(x) - 1
    while l <= r:
        if x[l] == x[r]:
            return False
        l += 1
        r -= 1

    return True
        
    
    
    
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))