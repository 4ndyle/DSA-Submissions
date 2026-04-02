# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Use a DFS and compare the result of the left and right subtrees

Base Case:
if root is empty:
    return True

Recursive case:
if abs(left - right) > 1:
    return False
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return max(left,right) + 1

        leftHeight = dfs(root.left)
        rightHeight = dfs(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
