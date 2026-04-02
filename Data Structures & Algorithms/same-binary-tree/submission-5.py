"""
Input:
    - Treenode : p
    - Treenode : q 
Output:
    - bool : whether or not the trees are equivalent 
Constraints:
    - equivalent : same structure and same values 
    - number of nodes: [0,100]
    - range of values: [-100,100]

Plan: 
Use a dfs on both trees and compare their values and structure 

Same Structure:
If both nodes exist or both nodes do not exist: same structure 
If only one of the nodes exist: return False 

Same Value:
If p.val == q.val

Cases:
p = [], q = []
return True 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p and not q: 
            return True 
        
        # compare structure 
        if not p or not q:  
            return False 

        # compare values of nodes
        if p.val != q.val:
            return False 

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right

