# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode : p
    - TreeNode : q
Output:
    - bool ; true if two binary trees are equivalent 
Constraints:
    - possible number of nodes: [0,100]
    - possible length of nodes: [-100,100]

Plan: DFS 
Base Case:
if one node exists and other does not:
    return False
if p.val != q.val:
    return False

Post order traversal:
left = isSameTree(root.left)
right = isSameTree(root.right)

return left and right
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right






