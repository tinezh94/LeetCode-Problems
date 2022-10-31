"""

110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

"""

def isBalanced(root):
    def dfs(root):
        if not root: return [True, 0]
        left, right = dfs(root.left), dfs(root.right)
        balance = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
        return [balance, 1 + max(left[1], right[1])]

    return dfs(root)[0]

print(isBalanced([3,9,20,null,null,15,7]))
print(isBalanced([1,2,2,3,3,null,null,4,4]))