"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

def containsDuplicate(nums):
    nums.sort()
    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
        
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(containsDuplicate([1,2,3,4]))