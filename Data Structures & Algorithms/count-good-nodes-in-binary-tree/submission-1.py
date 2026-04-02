# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfsHelper(root, currMaxNode) -> int:
            # base case 
            # if the root does not exist, return 0 since theres no good nodes
            if not root:
                return 0

            # recursive calls
            left = dfsHelper(root.left, max(currMaxNode, root.val))
            right = dfsHelper(root.right, max(currMaxNode, root.val))

            # process the current node 
            # if the current node is a good node, increment the good nodes
            if (root.val >= currMaxNode):
                return left + right + 1
            
            return left + right

        return dfsHelper(root, root.val)