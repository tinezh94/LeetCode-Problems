"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

def generate(numRows):
    res = [[1]]
    for i in range(numRows - 1):
        # assume theres a 0 at the beginning and at the end of the last row in res
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            # each number is the sum of the two number above it 
            row.append(temp[j] + temp[j + 1])
        res.append(row)
        
    return res
        


print(generate(5))