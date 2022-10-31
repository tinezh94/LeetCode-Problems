"""
1. Two Sum

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

"""

def twoSum(nums, target):
    visitedMap = {}

    for i, num in enumerate(nums):
        diff = target - num
        # print(diff)
        if diff in visitedMap:
            return [visitedMap[diff], i]

        visitedMap[num] = i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))