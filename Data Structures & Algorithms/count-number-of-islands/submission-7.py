"""
DFS 

directions = up, down, left, right
visited = set() 
numIslands = 0

def dfs(row, col):
    if (row,col) visited or out of bounds or '0':
        return 
    
    mark as visited 

    traverse through all 1's connecting to current island 
    for dr, dc in directions:
        dfs(row + dr, col + dc)

for row in len(grid):
    for col in len(grid[0]):
        if (row,col) has not been visited 
            dfs(row,col)
            count += 1

return count 
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()

        numIslands = 0

        def dfs(r, c):
            # base case 
            outOfBounds = r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])

            if outOfBounds or (r,c) in visited or grid[r][c] == '0':
                return 

            # mark current position as visited 
            visited.add((r,c))

            # visit neighboring 1's 
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == '1':
                    dfs(row,col)
                    numIslands +=1 

        return numIslands




