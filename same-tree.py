"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

# def isSameTree(p, q):
#     # if one of the nodes is null, they are not equal
#     if not p or not q:
#         return False
    
#     # if both nodes are null, they are equal
#     if not p and not q:
#         return True
    
#     # if the value aren't the same, they are not equal
#     if p.val != q.val:
#         return False
    
#     # recursively do the same for each level of nodes
#     return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    


def isSameTree(p, q):
    if not p or not q:
        return False
    
    if not p and not q:
        return True
    
    if p.value != q.value:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# print(isSameTree([1,2,3], [1,2,3]))