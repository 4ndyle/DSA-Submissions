"""
Input:
    - TreeNode : root
    - TreeNode : subRoot
Output:
    - bool : whether or not subRoot is a subtree of root

Subtree if it consists of a node in tree and all of this node's descendents
    - cannot have extra children, must be exact structure and node values

Constraints:
    - number of nodes: [1,100]
    - range of values: [-100,100]

Plan:
Use a dfs to search through the tree 

base case:
if root is None and subRoot is not None, return False (no matches found)
if both root and subROot are none, return True

recursive case:
if root.val == subRoot.val and their children are equal (potential match):
    call isSubtree(root.left,subRoot.left)
    call isSubtree(root.right,subRoot.right)
otherwise, traverse normally until we find a match
    call isSubtree(root.left, subRoot)
    call isSubtree(root.right, subRoot)

return left and right
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: if root is None, return False since we didn't find a matching subtree
        if not root:
            return False 

        # if we find a matching node, check if it contains the subtree 
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True 

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right 

    def isSameTree(self, root1, root2):
        # base case: if both nodes are none, return True 
        if not root1 and not root2:
            return True 
        
        if not root1 or not root2:
            return False 

        # if node at both roots are not equal return False 
        if root1.val != root2.val:
            return False 

        left = self.isSameTree(root1.left, root2.left)
        right = self.isSameTree(root1.right, root2.right)

        return left and right 


    