"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # dict will be used to map old nodes to new nodes 
        oldToNew = {}

        def dfsHelper(node):
            # if the node has already been visited, refer to its cloned copy 
            if node in oldToNew:
                return oldToNew[node]

            # create a new node for the old node and add its neighbors 
            newNode = Node(node.val)
            oldToNew[node] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfsHelper(neighbor))

            return newNode

        return dfsHelper(node)