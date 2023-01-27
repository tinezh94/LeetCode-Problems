"""
    Give a range of integers, determine how many numbers have no repeating digits. 
"""

def countNumbers(n, m):
    count = 0
    for i in range(n, m + 1):
        num = str(i)
        s = set(num)
        if len(s) == len(num):
            count+= 1
    
    return count
        

print(countNumbers(80, 120))
print(countNumbers(81, 121))