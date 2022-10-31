"""

235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

"""

def lowestCommonAncestor(root, p, q):
    currNode = root
    # lowest ancestor is where the split happens in the tree
    while currNode:
        if p.val < currNode.val and q.val < currNode.val:
            currNode = root.left
        elif p.val > currNode.val and q.val > currNode.val:
            currNode = root.right
        else: 
            return currNode



print(lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5], 2, 8))
print(lowestCommonAncestor([6,2,8,0,4,7,9,null,null,3,5], 2, 8))
