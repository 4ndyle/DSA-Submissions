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
    - List[List[int]] : each list is the node values of each level in zig zag order 
        - start with left to right, right to left, etc. 
Constraints:
    - number of nodes: [0,2000]
    - range of values: [-100,100]

Plan: BFS to find nodes on each level 

1. Create a boolean to keep track of whether the ordering of the current level is left to right or vice versa 
    - if the leftToRight: append the nodes to a list keeping track of current level from L to R 
    - else: append the nodes to a list keeping track of current level from R to L 
2. Return result 
"""

from collections import deque 

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # empty tree 
        if not root: 
            return []

        # bfs 
        queue = deque()
        queue.append(root)

        results = []
        leftToRight = True

        # while there are nodes to process 
        while queue: 

            # find all nodes in the current level 
            currLevelLength = len(queue)
            currLevelList = deque()

            # add each node to the current level sublist in the zipzag order 
            for i in range(currLevelLength):
                # process the current node and add its children to the queue 
                currNode = queue.popleft()
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)

                # add the node value to the current level list in the zig zag order 
                if leftToRight: 
                    currLevelList.append(currNode.val)
                else:
                    currLevelList.appendleft(currNode.val)

            # update the left to right ordering and add current level sublist to list result 
            leftToRight = not leftToRight
            results.append(list(currLevelList))

        return results