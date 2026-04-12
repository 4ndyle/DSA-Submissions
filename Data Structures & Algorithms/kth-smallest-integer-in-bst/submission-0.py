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
    - int: Kth smallest integer in BST 
Constraints:
    - number of nodes: [1,1000]
    - value of nodes: [0,1000]


"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kthSmallest = 0

        def dfsHelper(root): 
            if not root:
                return 

            nonlocal count 
            nonlocal kthSmallest

            # in order traversal 
            # process left subtree
            left = dfsHelper(root.left)

            # process the current node 
            count += 1

            if count == k:
                kthSmallest = root.val

            # process right subtree
            right = dfsHelper(root.right)

        dfsHelper(root)
        return kthSmallest


