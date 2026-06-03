class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        
        orignalColor = image[sr][sc]

        # create a dfs function traverse through the graph
        def dfs(row, col):
            # base case
            outOfBounds = row < 0 or row >= len(image) or col < 0 or col >= len(image[0])
            
            if outOfBounds or (row,col) in visited or image[row][col] != orignalColor: 
                return 

            # update the color of the current node, add node to visited, and call dfs on neighbors
            image[row][col] = color
            visited.add((row,col))
            
            for dr, dc in directions:
                dfs(row + dr, col + dc)        

        # call the dfs function on the starting node
        dfs(sr, sc)

        # return the image after modifyingge
        return image    
