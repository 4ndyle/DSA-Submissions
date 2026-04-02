# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: root 
Output: 
    - TreeNode: inverted binary tree 
Constraints:
    - number of nodes: [0,100]
    - value of nodes: [-100,100]

Plan: 
Use a DFS to traverse the tree and swap the left and right children of every node 
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case 
        if not root: 
            return

        # swap the left and right children
        root.left, root.right = root.right, root.left

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        return root 


