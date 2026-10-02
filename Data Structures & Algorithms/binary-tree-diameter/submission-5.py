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
    - int : diameter of the tree (length of the longest path between any 2 nodes)
Constraints:
    - path cannot include same node twice
    - possible number of nodes: [1,100]
    - possible values of nodes: [-100,100]

Plan: DFS 
Base Case:
if not root:
    return 0

Post Order Traversal
left = function(root.left)
right = function(root.right)

return left + right
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0 

        def dfs(root):
            nonlocal maxDiameter 

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            maxDiameter = max(left + right, maxDiameter)

            return max(left, right) + 1

        dfs(root)
        return maxDiameter




