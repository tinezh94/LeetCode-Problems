"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

def intersect(nums1, nums2):
    res = []
    map1 = {}
    for i in range(len(nums1)):
        map1[nums1[i]] = map1.get(nums1[i], 0) + 1
    
    for num in nums2:
        if map1.get(num, 0) > 0:
            res.append(num)
            map1[num] -= 1
    return res
    
print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4,9,5], [9,4,9,8,4]))