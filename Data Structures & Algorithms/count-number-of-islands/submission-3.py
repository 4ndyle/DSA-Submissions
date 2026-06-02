"""
Input:
    - List[List[int]] : grid
Output:
    - int : number of islands in the graph 
Constraints:
    - length of list: [1,100]
    - grid[i]: 0, 1
    - island: 1's that are connected adjacently horizontally or vertically 

Plan:
Go through each node in the graph and perform a dfs
when we encounter an 1 to mark the 1's that form an island
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()

        numberOfIslands = 0 

        def dfs(row, col):  
            # base case
            if (row, col) in visited:
                return
            
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 

            if grid[row][col] == "0":
                return

            # mark the current node as visited
            visited.add((row,col))

            # recursive case 
            # call dfs on neighbors 
            for dr, dc in directions:
                dfs(dr + row, dc + col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row, col)
                    numberOfIslands += 1

        return numberOfIslands