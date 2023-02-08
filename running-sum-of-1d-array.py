"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

def runningSum(nums):
    sum = 0
    res = []
    for i in range(len(nums)):
        sum += nums[i]
        res.append(sum)
    return res


print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))