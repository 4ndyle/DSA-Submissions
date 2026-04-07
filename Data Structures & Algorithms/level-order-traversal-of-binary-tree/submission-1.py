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
    - List[List[int]]: sublists of values of nodes at each particular level (from L to R)
Constraints:
    - number of nodes: [0,1000]
    - range of values: [-1000,1000]

Plan: 
BFs Search 
"""

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # bfs traversal 
        queue = deque()
        queue.append(root)
        
        res = []

        # while there are nodes to process in the tree 
        while queue: 
            # get the number of nodes in the current level 
            currLevelLength = len(queue)
            level = []
            
            # process all nodes in the current level 
            while currLevelLength > 0:
                currNode = queue.popleft()
                level.append(currNode.val)

                # add the left and right children of the current node to the queue to be processed later 
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)
                
                currLevelLength -= 1
                
            # add the sublist of the current level to the result 
            res.append(level)
            
        return res





        