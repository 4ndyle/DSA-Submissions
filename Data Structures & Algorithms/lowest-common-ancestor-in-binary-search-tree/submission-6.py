# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: root
    - TreeNode: p
    - TreeNode: q
Output:
    - TreeNode: lowest common ancestor of p and q
Constraints:
    - number of nodes: [2,100]
    - values of nodes: [-100,100]
    - p != q
    - p and q exist in the BST

Plan: DFS search (BST)

if p and q > root.val:
    traverse right
if p and q < root.val: 
    traverse left
if root.val between p and q
    return root
if root.val = p or q:
    return root
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = None

        if p.val > root.val and q.val > root.val:
            result = self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            result = self.lowestCommonAncestor(root.left, p, q)
        else:
            result = root
        
        return result






