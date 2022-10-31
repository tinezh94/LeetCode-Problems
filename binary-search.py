"""

704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""

def binarySearch(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        # Find the midpoint in nums
        mid = (left + right) // 2
        # if target is less than the number at midpoint, which means target is in the second half of nums, shift left pointer to mid + 1
        if nums[mid] < target:
            left = mid + 1
        # if target is greater than the number at midpoint, which means target is in the first half of nums, shift right pointer to mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else: 
            return mid

    return -1  

print(binarySearch([-1,0,3,5,9,12], 9))
print(binarySearch([-1,0,3,5,9,12], 2))