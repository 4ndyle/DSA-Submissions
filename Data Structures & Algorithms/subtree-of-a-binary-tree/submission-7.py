# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: root
    - TreeNode: subRoot

Output:
    - bool: if there is a subtree of root with the same structure/values of subRoot

Constraints:
    - number of nodes: [1,100]
    - range of values: [-100,100]

Plan: 
1. Define a function to check if 2 trees are equivalent or the same
    - both trees need the same STRUCTURE and VALUES 
2. Traverse through the root tree and check if the subRoot is a subtree of every node in the root tree 

# define a function for determining if both tree are the same 
def isSameTree(a, b) -> bool:
    # base case 
    if a and b are empty, return True 
    if only one node exsits, return False 

    # process the current node 
    if both nodes are not equal, return False and stop search 

    # recursive functions 
    call left and right subtrees 

    return left and right results 
"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case 
        if not root:
            return False 

        # process the current node 
        if self.isSameTree(root, subRoot):
            return True
        
        # recurisve functions 
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right 
        
    def isSameTree(self, a, b) -> bool: 
        # base case 
        if not a and not b:
            return True 
        
        # process the current node 
        if not a or not b:
            return False 
        
        if a.val != b.val:
            return False 

        # recursive calls 
        left = self.isSameTree(a.left, b.left)
        right = self.isSameTree(a.right, b.right)

        return left and right 
        