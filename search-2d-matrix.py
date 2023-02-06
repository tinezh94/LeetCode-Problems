"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    # top row, and bottom row to see where the target falls between
    trow, brow = 0, rows - 1
    
    #binary search for rows 
    while trow <= brow:
        # middle row 
        mrow = (trow + brow) // 2
        # if target is greater than the last value at matrix at mrow, move trow up by 1
        if target > matrix[mrow][-1]:
            trow = mrow + 1
        # if target is less than the first value at matrix at mrow, move brow down by 1
        elif target < matrix[mrow][0]:
            brow = mrow - 1
        else:
            break
    
    # if broke out of the loop, no values found return false
    if not (trow <= brow):
        return False
    
    # the row where the targe value is 
    row = (trow + brow) // 2
    
    # 2 pointers
    l, r = 0, cols - 1
    
    while l <= r:
        m = (l + r) // 2
        # if target greater than the value at m point, move l up 
        if target > matrix[row][m]:
            l = m + 1
        # if target less than value at m point, move r down 
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

             