"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

def missingNumber(nums):
    for i in range(len(nums)):
        nums.sort()
        if nums[i] != i:
            return i
    
    return len(nums)


print(missingNumber([3,0,1]))
print(missingNumber([0,1]))

print(missingNumber([9,6,4,2,3,5,7,0,1]))