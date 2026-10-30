"""
Input:
    - list[list[int]] : image 
    - int : sr
    - int : sc 
    - int : color 
Output:
    - list[list[int]] : image after performing the flood fill 
Constraints:
    - length of image: [] 
    - length of image[i]: []
    - possible values: []

Plan: 
Start at image[sr][sc] and perform a dfs from the current position. 
    - move to neighbor if it is the same as original color 
    - update color if it is the same as the original color 

Time: O(n*m)
Space: O(n*m)
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        visited = set() 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c): 
            # base case: if out of bounds or not original color, return 
            outOfBounds = r < 0 or r >= len(image) or c < 0 or c >= len(image[0])

            if outOfBounds or (r,c) in visited or image[r][c] != originalColor: 
                return 

            # process current position and mark current positon as visited
            if image[r][c] == originalColor: 
                image[r][c] = color

            visited.add((r,c))

            # visit neighbors 
            for dr, dc in directions: 
                dfs(dr + r, dc + c)

        dfs(sr, sc)
        return image 