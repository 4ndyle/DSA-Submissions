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

# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        queue = deque()
        if root: queue.append(root)

        while queue: 
            levelLength = len(queue)
            
            for i in range(levelLength):
                currNode = queue.popleft()

                # add last node to results 
                if i == levelLength - 1: results.append(currNode.val)

                # add children of current node to process 
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)

        return results