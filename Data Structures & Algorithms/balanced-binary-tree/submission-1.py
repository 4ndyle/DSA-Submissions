# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input: root 
Output: boolean (balanced or not balanced)
Edge Cases: 
    - empty tree: true
    - one node: true

Plan: Use recursion to find the max depth of the left and right subtrees and compare them. If their heights differ
by more than 1, we know that it is not balanced and return False

Base Case

if root is empty:
    return 

Write a dfs function
left = dfs(root.left)
right = dfs(root.right)


"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return max(left, right) + 1

        left = dfs(root.left)
        right = dfs(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

