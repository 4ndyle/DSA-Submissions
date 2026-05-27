"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Input:
    - Node: a node in the graph
Output:
    - Node: a deep copy of the node in the grpah along with all of its neighbors
Constraints:
    - number of nodes: [0,100]
    - values of nodes: [1,100]
    - no duplicate edges or self loops in the graph

Plan:
Use DFS to go through the starting node and each node and create a copy of each node
we have not visited

1. Create a dict to map oldNode : newNode (so we can connect nodes we have already visited)
2. Create a recursive DFS function to go through each node
    - if the current node has already been visited, return the newNode copy
    - otherwise:
        - create a new node as a copy of the current old now
        - add the mapping to the dict
        - for each neighbor of the current node:
            - call the dfs function on it
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(currNode):
            if currNode in oldToNew:
                return oldToNew[currNode]

            # create the new node with the val
            newNode = Node(currNode.val)
            oldToNew[currNode] = newNode

            # add neighbors for the new node
            for neighbor in currNode.neighbors:
                newNeighbor = dfs(neighbor)
                newNode.neighbors.append(newNeighbor)
            
            return newNode

        dfs(node)
        return oldToNew[node]

