"""
Given an integer array nums, find the subarray
which has the largest sum and return its sum.
"""

def maxSubarray(nums):
    currSum = 0
    maxSum = nums[0]
    
    for i in range(len(nums)):
        if currSum < 0:
            currSum = 0
            
        currSum += nums[i]
        maxSum = max(maxSum, currSum)
    
    return maxSum
    

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubarray([5,4,-1,7,8]))