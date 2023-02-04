"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""

def merge(nums1, m, nums2, n):
    # 3 pointers: l last index of nums1 with validate integers, r last index of nums2, k last index of merged arrays(in this case, m)
    l, r, k = m - 1, n - 1, m + n - 1

    while l >= 0 and r >= 0:
        if nums1[l] > nums2[r]:
            nums1[k] = nums1[l]
            l -= 1
        elif nums1[l] < nums2[r]:
            nums1[k] = nums2[r]
            r -= 1
        else:
            nums1[k] = nums2[r]
            k -= 1
            r -= 1
            nums1[k] = nums1[l]
            l -= 1
        k -= 1

    while l >= 0:
        nums1[k] = nums1[l]
        l -= 1
        k -= 1
    
    while r >= 0:
        nums1[k] = nums2[r]
        r -= 1
        k -= 1
        
    return nums1
    

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))