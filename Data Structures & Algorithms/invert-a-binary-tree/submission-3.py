"""
Input:
    - TreeNode : root 
Output: 
    - TreeNode : root of inverted binary tree
Constraints:
    - number of nodes in tree : [0,100]
    - range of values : [-100,100]

Plan:

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case 
        # if the root does not exist, return 
        if not root:
            return 

        # recursive case 
        left = root.left
        right = root.right

        root.right = left
        root.left = right

        self.invertTree(root.left)
        self.invertTree(root.right) 

        return root 
