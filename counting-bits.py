"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

"""

def countingBits(n):
    offset = 1
    #dp array initialized with a 0 because all arrays will start at 0, and will have length of n + 1
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    
    return dp
    
print(countingBits(2))
print(countingBits(5))