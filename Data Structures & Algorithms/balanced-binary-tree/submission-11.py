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
    - bool: true if tree is heigh-balanced 

Plan:

"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # post order traversal
        def dfs(root):
            if not root:
                return (0, True)

            left = dfs(root.left)
            right = dfs(root.right)

            if not left[1] or not right[1] or abs(left[0] - right[0]) > 1:
                return (max(left[0],right[0]) + 1, False)
            
            return (max(left[0],right[0]) + 1, True)

        result = dfs(root)
        return result[1]

            