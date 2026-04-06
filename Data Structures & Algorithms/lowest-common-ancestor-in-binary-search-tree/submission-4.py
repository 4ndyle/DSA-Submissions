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
    - TreeNode: lowest common ancestor between p and q 
Constraints:
    - number of nodes: [2,100]
    - range of values: [-100,100]
    - p != q 
    - p and q are garanteed to exist in the BST 

if p or q are children of each other, then the highest in the tree is the LCA


Conditons to consider:
1. if both p and q are less than the current node: traverse left 
2. if both p and q are greater than the current node: traverse right 
3. if p or q are split where one node is less than and one node is greater than the current node, then the cuurrent node is the LCA 
4. if p or q equal to the current node: then the current node is the LCA 
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base case 
        if p.val == root.val or q.val == root.val:
            return root
                
        # recursive cases to process current node 
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)

        return root





        