"""
Input:
    - List[List[str]] : grid ('1' = land)
Output
    - int : number of islands 
Constraints:
    - length of grid = [1,100]
    - length of grid[i] = [1,100] 
    - all rows in grid are equal? 
    - grid[i] = "1" or "0" 

Plan: DFS
1. Create variables 
    - numberOfIslands = 0 
    - visited = set() 
    - directions = up, down, left, right 
2. dfsHelper(row, col)
        if (row, col) visited or outOfBounds or 0:
            return 
        
        mark as visited 

        for dr, dc, in directions:
            dfsHelper(row + dr, col + dc)

        return 1 
3. Visit each position (row, col) and call the dfsHelper on the position and update numberOfIslands 
4. Return numberOfIslands 
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() 
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        rows = len(grid)
        cols = len(grid[0])

        def dfsHelper(r, c):
            # base case: visited or out of bounds or water 
            outOfBounds = r < 0 or r >= rows or c < 0 or c >= cols

            if (r,c) in visited or outOfBounds or grid[r][c] == "0":
                return 0

            # mark as visited 
            visited.add((r,c))

            # visit each neighbor 
            for dr, dc in directions:
                dfsHelper(r + dr, c + dc)

            return 1
        
        # count the number of islands 
        numberOfIslands = 0 

        for row in range(rows):
            for col in range(cols):
                numberOfIslands += dfsHelper(row,col)

        return numberOfIslands 





