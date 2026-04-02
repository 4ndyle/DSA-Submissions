# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input: root
Output: integer (count of good nodes)
Constraints:
    - a good node is a node that has no nodes greater than it from
    the root of the tree to the node
Edge Cases:
    - empty root -> 0
    - one root -> return 1

Plan:
goodNodesCount = 0

def dfs(root, currentMax):
    Base Case
    if the root is empty:
        return 

    Recursive Condition Cases
    if the current root value is greater than or equal to the currentMax:
        increment the count of goodNodes

    call the dfs on the left subtree
    call the dfs on the right subtree

dfs(root, root.val)
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCount = 0

        def dfs(root, currentMax):
            nonlocal goodNodesCount
            
            # Base Case
            if not root:
                return

            # Recurive conditional cases
            if root.val >= currentMax:
                goodNodesCount += 1
                currentMax = root.val

            dfs(root.left, currentMax)
            dfs(root.right, currentMax)
        

        dfs(root, root.val)

        return goodNodesCount


            
