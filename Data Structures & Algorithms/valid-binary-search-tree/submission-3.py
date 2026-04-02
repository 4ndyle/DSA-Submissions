# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(root, minPossibleVal, maxPossibleVal) -> bool:
            # base case 
            # if the root does not exist, it is still a valid bst and we have checked all nodes 
            if not root:
                return True 

            # pre order DFS 
            # process the current node 
            if not (root.val < maxPossibleVal) or not (root.val > minPossibleVal):
                return False 

            left = isValidBSTHelper(root.left, minPossibleVal, root.val)
            right = isValidBSTHelper(root.right, root.val, maxPossibleVal)

            return left and right

        return isValidBSTHelper(root, -float("inf"), float("inf"))