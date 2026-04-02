# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Base Case:
if both trees are empty:
    return True
if not p or not q:
    return False 

Recursive Case
if p != q:
    return False

left = isSameTree(p.left, q.left)
right isSameTree(p.right, q.right)

return left and right
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case
        if not p and not q:
            return True
        if not p or not q:
            return False

        # Recursive Case
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right
        