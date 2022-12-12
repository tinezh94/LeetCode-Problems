"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
"""

def sortedArrayToBst(nums):
    def dfs(l, r):
        if l > r:
            return None
        
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = dfs(l, m - 1)
        root.right = dfs(m + 1, r)
        return root
    
    return dfs(0, len(nums) - 1)