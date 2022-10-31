"""

226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

"""

def invertBinaryTree(root):
    if not root:
        return None
    
    lnode = root.left
    root.left = root.right
    root.right = lnode

    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    return root


print(invertBinaryTree([4,2,7,1,3,6,9]))
print(invertBinaryTree([2,1,3]))
print(invertBinaryTree([]))