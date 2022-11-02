"""
543. Diameter of binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

"""

def diameterOfBinaryTree(root):
    res = [0]
    
    def dfs(root):
        if not root:
            return -1
        
        lft = dfs(root.left)
        rht = dfs(root.right)
        res[0] = max(res[0], 2 + lft + rht)
        
        return 1 + max(lft, rht)
    
    dfs(root)
    return res[0]
    
print(diameterOfBinaryTree([1,2,3,4,5]))
print(diameterOfBinaryTree([1,2]))