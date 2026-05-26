
"""
Input:
    - List[List[str]]: grid
Output:
    - int : number of islands
Constraints;
    - length of row and cols: [1,100]
    - grid[i][j] = 0 or 1

Plan: Use a BFS to search the graph, and mark each island (1) as visited when we 
encounter a node that is connected to that island

1. 
"""

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # set up the graph logisitcs
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        visited = set()
        islands = 0 

        # BFS search on the graph
        # create a helper function to perform a bfs 
        def bfsHelper(position):
            queue = deque()
            queue.append(position)

            while queue:
                currPosition = queue.popleft()

                # check all neighbors of the current node and process all connected 1's
                # to mark the whole island as visited
                for dr, dc in directions:
                    nr = currPosition[0] + dr
                    nc = currPosition[1] + dc

                    # if the neigbor's position is in the grid and it is a 1, add to queue
                    validPosition = nr >= 0 and nr < rows and nc >= 0 and nc < cols

                    if validPosition and grid[nr][nc] == "1" and currPosition not in visited:
                        queue.append((nr, nc))

                visited.add(currPosition)

        # go through each grid position
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfsHelper((i,j))
                    islands += 1

        return islands

