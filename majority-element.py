"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""

from collections import Counter

def majorityElement(nums):
    count = Counter(nums)
    
    for key in count:
        if count[key] > len(nums) / 2:
            return key
    

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))