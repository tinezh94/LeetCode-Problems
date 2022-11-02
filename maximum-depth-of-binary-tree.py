"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
from collections import deque

# def maxDepth(root):
#     stack = [[root, 1]]
#     res = 0
#     # BFS Iterative 
#     while stack:
#         node, depth = stack.pop()
        
#         if node:
#             res = max(res, depth)
#             stack.append([node.left, depth + 1])
#             stack.append([node.right, depth + 1])
            
#     return res


def maxDepth(root):
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    level += 1
    return level
    