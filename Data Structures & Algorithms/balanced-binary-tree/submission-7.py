# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # create a dfs function to find the result in the form of 
        # [isBalanced, height]

        def dfs(root):
            # base case
            if not root:
                return [True, 0]

            # recursive case
            # find the height and balanced of the left and right subtree 
            left, right = dfs(root.left), dfs(root.right)

            # check if the left and right subtree are balanced
            balancedSubtrees = left[0] and right[0]
            heightDifference = abs(left[1] - right[1])

            return [balancedSubtrees and heightDifference <= 1, max(left[1],right[1]) + 1]

        res = dfs(root)
        return res[0]