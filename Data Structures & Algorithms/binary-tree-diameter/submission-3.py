"""
Input:
    - TreeNode : root 
Output:
    - int : diameter of the tree 

Diameter: length of the longest path between any two nodes within the tree 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # create a variable to keep track of the max diameter 
        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter 

            # if the root is None, return 0 
            if root is None:
                return 0 

            # search the left subtree to find the max diameter 
            left = dfs(root.left)

            # search the right subtree to find the max diameter
            right = dfs(root.right)

            # calculate the max diameter from the current node and update the maxDiameter value if greater than 
            maxDiameter = max(left+right, maxDiameter)

            return max(left, right) + 1

        # call the recursive function
        dfs(root)

        return maxDiameter