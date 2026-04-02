# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode : root 
Output:
    - int : max depth of the binary tree (longest path from the node down to the farthest leaf node)
Constraints:
    - number of nodes: [0,100]  
    - range of values: [-100,100]

Plan: Perform a post order dfs serach on the tree to find the max depth of the tree 
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case 
        if not root:
            return 0

        # recursive calls 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
        

        