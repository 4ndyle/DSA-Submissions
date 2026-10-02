# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: root 
Output:
    - List[int] : node values visible from right side of tree 
Constraints:
    - possible number of nodes: [0,100]
    - possible values of nodes: [-100,100]

Plan: 

DFS - use a height variable to keep track of max height and only add nodes 
when the node at level x > maxHeight 

BFS - traverse tree level by level and add last node in each level to result 
"""

# DFS 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        maxHeight = -1 
        results = []

        def dfs(root, currHeight):
            # base case 
            if not root:
                return 
            
            # pre order traversal 
            nonlocal maxHeight
            if currHeight > maxHeight: 
                results.append(root.val)
                maxHeight = currHeight

            right = dfs(root.right, currHeight + 1)
            left = dfs(root.left, currHeight + 1)

            return 
        
        dfs(root, 0)
        return results




