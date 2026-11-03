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

