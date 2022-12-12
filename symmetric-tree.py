"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""

def symmetricTree(root):
    if not root: return True

    def dfs(leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        if not leftroot or not rightroot:
            return False
        
        if leftroot.val == rightroot.val:
            return dfs(leftroot.left, rightroot.right) and dfs(leftroot.right, rightroot.left)
            
    return dfs(root.left, root.right)