# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input: root 
Output: list (nodes that are visible from the right side of the tree, top to bottom)
Constraints: 
    - visible from right side of tree
    - ordered top to bottom
Edge Cases
    - empty root -> return []
    - one root -> return [root.val]

Plan: Create a list to store results and a variable to keep track of the depth. Use a DFS
on the right subtree first and update the depth. Only add nodes to the result list if it is 
equal to the depth. Calling the right tree first will ensure nodes in the right are added
before the left tree is checked. The recursive function will keep track of the current depth.

Base Case:
result = []
depth = 0

def dfs(root, currentDepth):
    if not root:
        return
    if currentDepth equals depth, add the current node to the result list

    recursively call the dfs on right subtree and update currentDepth
    recursively call the dfs on left subtree and update currentDepth

call the dfs function on the root
return result
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        depth = 0

        def dfs(root, currentDepth):
            nonlocal depth
            if not root:
                return []

            if currentDepth == depth:
                result.append(root.val)
                depth += 1

            dfs(root.right, currentDepth+1)
            dfs(root.left, currentDepth+1)

        dfs(root, depth)
        return result

        