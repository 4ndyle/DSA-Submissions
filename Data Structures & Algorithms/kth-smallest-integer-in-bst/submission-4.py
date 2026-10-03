# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: root 
    - int: k 
Output:
    - int: kth smallest node in the tree (1 indexed)
Constraints:
    - possible number of nodes: [1,10000]
    - possible values of nodes: [0,10000]
    - possible values of k: [1, number of nodes]

Plan: Use a DFS and add each node in-order to a list and return the k-1th node in the list 
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = -1

        def dfsHelper(root):
            nonlocal result 

            # base case 
            if not root or result != -1:
                return

            # in-order DFS traversal
            left = dfsHelper(root.left)

            nonlocal count
            count += 1
            
            if count == k: result = root.val

            right = dfsHelper(root.right)
            return 

        dfsHelper(root)
        return result

