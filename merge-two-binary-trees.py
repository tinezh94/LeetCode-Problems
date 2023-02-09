"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

def mergeTrees(root1, root2):
    if not root1 and not root2: return None
    
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    
    root = TreeNode(v1 + v2)
    
    root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    
    return root