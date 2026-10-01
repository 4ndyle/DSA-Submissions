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
    - TreeNode: root of inverted binary tree 
Constraints:
    - possible values of nodes: [-100, 100]
    - possible number of nodes: [0,100]

Plan: DFS 

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None 

        # post order traversal
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


