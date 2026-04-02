# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:  
    - TreeNode : root of the binary tree
Output: 
    - bool : whether or not a tree is balanced (height differs by more than one)
Constraints:
    - range of values for each node : -1000 <= x <= 1000
    - number of nodes in a bst : [0,1000]
Edge Cases:
    - 0 nodes -> return True 
    - chain of nodes (left or right heavy) : return False
    - difference in height left and right subtrees <= 1 : return True

Plan: Use a DFS to get the height of the right and left subtrees and compare their heights. 
If their heights differ by more than one, return False.
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

            return  max(left, right) + 1

        leftHeight = dfs(root.left)
        rightHeight = dfs(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        # call for every subtree in the binary tree
        return self.isBalanced(root.left) and self.isBalanced(root.right)


