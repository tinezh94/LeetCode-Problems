"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            if l == r: return m + 1
            l = m + 1
        elif nums[m] > target:
            if l == r: return m
            r = m
        else:
            return m
    
    


print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))