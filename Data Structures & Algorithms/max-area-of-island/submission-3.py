class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()

        currArea = 0

        def dfs(r, c):
            outOfBounds = r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])

            if outOfBounds or (r,c) in visited or grid[r][c] == 0:
                return 

            # mark position as visited and increment island area 
            visited.add((r,c))
            nonlocal currArea
            currArea += 1

            # visit neghbors
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        maxArea = 0 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dfs(row,col)
                maxArea = max(maxArea, currArea)
                currArea = 0 

        return maxArea
                