"""
Input:
    - List[List[int]] : grid
Output:
    - int : max area of the islands
Costraints: 
    - length of grid: [1,50]
    - value of grid[i]: 0,1
Edges Cases:
    - if no islands, return 0 

Plan: 

Variables:
    - maxArea
    - directions
    - visited 

Use a DFS and pass in the (row, col, currArea)
    - if the current node is 1, increment the currAra
    - otherwise, the current node is a 0, set currArea = 0
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # up, down, left, right
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        def dfs(row, col):
            # base case
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            if (row, col) in visited or grid[row][col] == 0:
                return 0

            visited.add((row,col))
            
            area = 1
            # process the other nodes, prioritize 1's
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                area += dfs(nr,nc)
                
            return area

        maxArea = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxArea = max(maxArea, dfs(r,c))

        return maxArea
