"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums):
    res = []
    nums.sort()
    # print(nums)
    for index, num in enumerate(nums):
        if index > 0 and num == nums[index - 1]:
            continue
        
        l, r = index + 1, len(nums) - 1
        while l < r:
            threeSum = num + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    
    return res
         
                


print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,1,1]))
# print(threeSum([0,0,0]))