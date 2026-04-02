# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input: root 
Output: integer (diameter - length of the longest path)
Edge Cases:
    - one node -> return 1

Plan: Use a DFS traversal to find the max depth of each subtree. The longest length will be the sum of the left
and right subtree or a previous result. 
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(root):
            if root is None: 
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left + right)

            return max(left,right) + 1

        dfs(root)
    
        return self.result

        