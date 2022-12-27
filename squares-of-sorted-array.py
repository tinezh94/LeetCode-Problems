"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    return nums


print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))