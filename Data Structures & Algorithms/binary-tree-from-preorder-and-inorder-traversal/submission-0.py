# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - List[int] : preorder
    - List[int] : inorder 
Output:
    - TreeNode : binary tree from the preorder and inorder traversals 

preorder : root left right 
inorder : left root right 

Example 1: 
preorder = [1,2,3,4]
inorder = [2,1,3,4]


"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None 

        # create the root for the subtree and set the root to be the first value in the preorder 
        root = TreeNode(preorder[0])

        # call the function recursivley for the left and right subtree
        # split the partition of the left/right by finding where the root value occurs in the inorder list 
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root 



        
