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
    - List[int]: values of nodes that are visible from the right side of the tree
Constraints:
    - number of nodes: [0,100]
    - range of values: [-100,100]

Plan:
Use a BFS level order traversal. At each level add the last node value to the result 
since that is the furthest most right node in the current level
"""

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # BFS 
        queue = deque()
        queue.append(root)

        rightmostNodes = []

        # while there are nodes left to process
        while queue:
            currLevelLength = len(queue)
            currLevelNodes = []

            # go through each node in the current level
            for i in range(currLevelLength):
                currNode = queue.popleft()
                currLevelNodes.append(currNode)

                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)

            # add the rightmost node into the results
            rightmostNodes.append(currLevelNodes[-1].val)

        return rightmostNodes



