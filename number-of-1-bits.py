"""
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

"""

def hammingWeight(n):
    res = 0
    
    while n:
        res += n % 2
        n = n >> 1
    
    return res
    
# print(hammingWeight(00000000000000000000000000001011))
# print(hammingWeight(00000000000000000000000010000000))
# print(hammingWeight(11111111111111111111111111111101))