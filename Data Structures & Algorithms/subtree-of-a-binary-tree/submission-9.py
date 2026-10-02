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
    - bool : true if subroot with same structure and values in root
Constraints:
    - number of nodes in root: [1,2000]
    - number of nodes in subRoot: [1,1000]
    - values in root: [-10^4, 10^4]
    - values in subRoot: [-10^4, 10^4]

"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        containsTree = False

        # post order travaersal
        def dfs(root, subRoot):
            if not root:
                return

            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)

            # process current node
            if self.isSameTree(root, subRoot):
                nonlocal containsTree
                containsTree = True

            return

        dfs(root, subRoot)
        return containsTree

    def isSameTree(self, p, q):
        # base case
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
        
