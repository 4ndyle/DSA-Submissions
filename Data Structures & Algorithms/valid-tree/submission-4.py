"""
Input:
    - int: n
    - List[List[int]]: edges
Output:
    - bool: whether or not the edges make up a valid tree
Constraints:
    - range of values: [0,n-1]
    - number of nodes: [1,100]
    - no duplicate edges

A graph is a valid tree if:
    - graph does not contain any cycles
    - should be able to reach all other nodes from a single node

Plan:
1. Convert the list of edges into a adjacency list
2. Perform a dfs on the node
    - if we encounter a node that we have already visited, return False
3. If we have visited all nodes, return True, otherwise False
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:   
        if not edges:
            return True

        # convert the list of edges -> adjacency list
        nodes = [[] for i in range(n)]
        print(nodes)

        for source, destination in edges:
            nodes[source].append(destination)
            nodes[destination].append(source)

        print(nodes)

        # perform a dfs on a single node and keep track of visited
        visited = set()
        containsCycle = False

        def dfs(currNode, parent):            
            # if the node has already been visited, there is a cycle
            if currNode in visited:
                nonlocal containsCycle
                containsCycle = True 
                return
        
            visited.add(currNode)

            # visit the neighbors of the current node
            for neighbor in nodes[currNode]:
                # skip nodes that loop back to parent since it undirecteed graph
                if neighbor == parent:
                    continue
                
                dfs(neighbor, currNode)

        dfs(edges[0][0],-1)

        # check if every node has been visited
        allNodesVisited = len(visited) == n

        return not containsCycle and allNodesVisited






