"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

def reshapeMatrix(mat, r, c):
    m, n = len(mat), len(mat[0])
    
    if m*n != r*c:
        return mat
    
    flatten = []
    # flatten mat into 1-D array
    for row in mat:
        for num in row:
            flatten.append(num)
        
    print(flatten)
    k = 0
    
    # 0 as place holder making a new matrix with r and c
    res = [[0 for i in range(c)] for j in range(r)]
    print(res)
    # replace each 0 with the number in flatten array
    for i in range(r):
        for j in range(c):
            res[i][j] = flatten[k]
            k += 1
    
    return res       
        


print(reshapeMatrix([[1,2], [3,4]], 1, 4))