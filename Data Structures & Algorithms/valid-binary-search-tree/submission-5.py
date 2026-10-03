# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode:  root 
Output:
    - bool: true if valid binary search tree 
Constraints:
    - valid if left < root, right < root, left and right are also bst
    - possible number of nodes: [1,10000] 
    - possible values of nodes: [-10^6, 10^6]

Plan: Use DFS and check if node is within min and max values 
Base Case:
    if root None:
        return True
    if currNode val is not within bounds:
        return False 

When we traverse left:
    update max to be currNode.val
When we traverse right: 
    update min to be currNode.val
"""
from collections import deque 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfsHelper(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False 

            left = dfsHelper(root.left, minVal, root.val)
            right = dfsHelper(root.right, root.val, maxVal)

            return left and right 

        return dfsHelper(root, -float("inf"), float("inf"))


