"""
Input:
    - TreeNode: root
Output:
    - int : max depth of the tree 

depth: number of nodes along a path from the root down to the leaf of a tree 

Plan: Use a DFS to traverse the longest path and return the longest path from the two subtrees
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: if the root is empty, return 0 
        if root is None:
            return 0

        # process the left subtree, and return its depth
        left = self.maxDepth(root.left)

        # process the right subtree, and return its depth
        right = self.maxDepth(root.right)

        # return the max depth between the left/right tree and add 1 for the current node 
        return max(left, right) + 1
