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
    - List[List[int]] : level order traversal as nested list 
Constraints:
    - possible number of nodes: [0,2000]
    - possible values of nodes: [-1000,1000]

Plan: BFS 

result = []
queue = deque()
add root node to queue 

while queue:
    totalNodes = len(queue)
    currLevel = []

    for i in range(totalNodes):
        pop from front of queue and add node to current level
        add children of current node to queue 

    add currLevel to result list 

return result 
"""
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[eTreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        if root: queue.append(root)

        while queue:
            totalNodes = len(queue)
            currLevel = []

            for i in range(totalNodes):
                currNode = queue.popleft()
                currLevel.append(currNode.val)

                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)

            res.append(currLevel)

        return res 





