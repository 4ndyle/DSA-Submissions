"""
Input:
    - list[list[int]] : heights
        heights[r][c]: height above sea level 
Outut:
    - list[list[int]] : 2D list of coordinates of positions that can reach both oceans
Constraints:
    - rain water can flow to neighboring cells north, south, west, east if <= current cell value
    - length of heights: [1,200]
    - length of heights[i]: [1,200]
    - values of heights: [0,10^5]

Plan: 
1. Create a 2 sets to keep track of positions in the pacific/atlantic oceans
2. Visit the border of the heights and performa dfs from each border position
and only move to a cell if it is >= the current height (backwards traversal)
    - if we start from the top/left edge, then it will in the pacific set
    - if we start from the right/bottom edge, then it will in the pacific set
3. Return a list of positions that are in both the pacific and atlantic sets
"""

class Solution:
    def pacificAtlantic(self, theights: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        pacificSet = set()
        atlanticSet = set()

        def dfs(r,c, prevHeight, setName):
            # base case: out of bounds
            outOfBounds = r < 0 or r >= len(theights) or c < 0 or c >= len(theights[0])
            if outOfBounds or prevHeight > theights[r][c]:
                return
            if setName == "pacific" and (r,c) in pacificSet:
                return
            if setName == "atlantic" and (r,c) in atlanticSet:
                return

            # process current node
            if setName == "pacific":
                pacificSet.add((r,c))
            else:
                atlanticSet.add((r,c))

            # visit neighbors
            for dr, dc in directions:
                dfs(r + dr, c + dc, theights[r][c], setName)


        # go through border 
        for row in range(len(theights)):
            for col in range(len(theights[0])):
                if row == 0 or col == 0:
                    dfs(row, col, -1, "pacific")
                if row == len(theights) - 1 or col == len(theights[0]) - 1:
                    dfs(row, col, -1, "atlantic")

        return list(pacificSet & atlanticSet)

