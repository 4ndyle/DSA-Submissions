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
    - int : max number along the longest path of the tree 
Constraints:
    - possible values of nodes: [-100,100]
    - possible number of nodes: [0,100]

Plan: DFS 
Base Case:
    if root is None:
        return 0

Post Order Traversal 
left = maxDepth(root.left)
right = maxDepth(root.right)

return max(left, right)
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case 
        if not root:
            return 0

        # post order traversal 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1