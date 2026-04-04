# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: p
    - TreeNode: q 

Output:
    - bool : whether or not the trees are equivalent 

    equivalent:
        - exact same structure
        - same node values 

Constraints
    - range of values (p and q): [-100,100]
    - number of nodes (p and q): [0,100]

------------

Plan: Pre-Order DFS 

# base case (same structure)
1. If the p and q are both empty: return True (equal structure and value)
2. If only one of the trees are empty: return False (unequal structure)

# process the current node (same value)
1. If the node value in p and q are not the same, return False to stop the search 

# recursive DFs calls 
left = isSameTree(p.left, q.right)
right = isSameTree(p.right, q.right)

return left and right (both subtrees are the same)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case 
        if not p and not q:
            return True 
        
        if not p or not q:
            return False 
        
        # process the current node 
        if p.val != q.val:
            return False 

        # recursive calls 
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right



