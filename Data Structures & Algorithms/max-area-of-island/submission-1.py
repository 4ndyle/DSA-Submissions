"""
Input:
    - List[List[int]] : grid
Output:
    - int : max area of an island 
Constraints:
    - grid[i] is either 0 or 1 (1 = land)
    - possible length of grid: [1,50]
    - possible length of grid[i]: [1,50]

Plan: DFS on each island 
1. Create variables
    - directions = up, down, left, right
    - visited = set()
    - maxArea = 0 
2. dfsHelper(row, col):
        if (row, col) in visited or grid[row][col] == 0 or out of bounds:
            return 0 
        
        add (row, col) to visited
        land = 1

        for dr, dc in directions:
            land += dfsHelper(row + dr, col + dc)

        return land
3. for row in range(len(grid)):
        for col in range(len(grid[i])):
            if (row, col) not in visited:
                maxArea = max(dfsHelper(row, col), maxArea)
4. return maxArea
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        maxArea = 0

        def dfsHelper(row, col):
            outOfBounds = row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])
            if outOfBounds or (row,col) in visited or grid[row][col] == 0:
                return 0

            # mark the current spot
            visited.add((row,col))
            land = 1

            for dr, dc in directions:
                land += dfsHelper(row + dr, col + dc)

            return land

        # go through all islands
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    maxArea = max(maxArea, dfsHelper(row,col))

        return maxArea
                    



            


