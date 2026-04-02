# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

"""
Input: root 
Output: boolean (true if valid binary search tree)
Constraints:
    - left subtree < root
    - right subtree > root
    - left and right subtrees are also bst
Edge Cases:
    - empty root -> return True
    - one root -> return True

Plan: use a DFS function to validate the left and right subtrees by using the root value
as either the low or high in the paramters for the function. (root, low, high)

Base Case:
if root is empty, return True

def dfs(root, low = -inf, high = inf):
    if not root:
        return True
    if not root value > low or not root value < high:
        return False

    call the function on left subtree with high = root.val
    call the function on right subtree with low = root.val

    return left result AND right result

return dfs(root), where it will be true if both the left and right subtrees are true
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root, low=float('-inf'), high=float('inf')):
            if not root:
                return True
            if not root.val > low or not root.val < high:
                return False

            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            return left and right

        return dfs(root)

        