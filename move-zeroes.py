"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
    

def moveZeroes(nums):
    for i in range(len(nums))[:-1]:
        if nums[i] == 0:
            # print(nums.pop(i))
            nums.pop(i)
            # print(nums.append(0))
            nums.append(0)
    return nums
            



# print(moveZeroes([0,1,0,3,12]))
# print(moveZeroes([0]))
print(moveZeroes([0,0,1]))