# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        totalGoodNodes = 0 

        def dfs(root, maxHeight):
            # base case 
            if not root:
                return
            
            # pre order traversal 
            if root.val >= maxHeight:
                nonlocal totalGoodNodes
                totalGoodNodes += 1
                
                maxHeight = root.val

            left = dfs(root.left, maxHeight)
            right = dfs(root.right, maxHeight)

            return 
        
        dfs(root, -float("inf"))
        return totalGoodNodes