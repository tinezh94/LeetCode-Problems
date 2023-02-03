"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

def rotateArray(nums, k):
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    reverseNums(nums, l, r)
    reverseNums(nums, l, k - 1)
    reverseNums(nums, k, r)
    return nums
    

def reverseNums(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    

print(rotateArray([1,2,3,4,5,6,7], 3))
print(rotateArray([-1,-100,3,99], 2))