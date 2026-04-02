"""
Input:
    - TreeNode : root
Output:
    - bool : whether or not the binary tree is balanced 

Balanced: height of left and right subtree differ by no more than 1

Contraints:
    - number of nodes: [0,100]
    - range of values: [-1000,1000]


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base case 
        # if the root does not exist, return true 
        if root is None:
            return True 

        # find the height of the left subtree
        leftHeight = self.heightDfs(root.left)

        # find the height of the right subtree 
        rightHeight = self.heightDfs(root.right)

        difference = abs(leftHeight - rightHeight)

        return difference <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def heightDfs(self, root) -> int: 
        # if the node is None, return 0
        if root is None:
            return 0 

        # find the height of the left subtree 
        left = self.heightDfs(root.left)

        # find the height of the right subtree
        right = self.heightDfs(root.right)

        return max(left,right) + 1