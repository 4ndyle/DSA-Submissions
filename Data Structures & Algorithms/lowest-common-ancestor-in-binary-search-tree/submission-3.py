# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input: two nodes (p and q)
Output: integer (lowest node in a tree such that both p and q are descendents)
Constraints:
    - ancestor is allowed to be a descendent of itself
Edge Cases:
    - empty root -> return None
    - one root -> return root.val

Plan: use a DFS traversal and traverse down a subtree (left or right) if p and q
are both LESS than the current root or GREATER than the current root. 

Psuedo Code: 
if root is empty, return none

define a dfs function(root):
    if root is empty, return None

    if p and q are both less than root.val:
        recursively call function on left subtree
    if p and q are both greater than root.val:
        recursively call function on right subtree
    
    otherwise return the root.val
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return None

            if p.val < root.val and q.val < root.val:
                return dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right)

            return root

        return dfs(root)
