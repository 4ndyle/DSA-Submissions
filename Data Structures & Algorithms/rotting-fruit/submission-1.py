"""
Input:
    - list[list[int]] : grid 
Output:
    - int : min number of minutes that must elapse until no cell has a fresh orange 
Constraints:
    - 0: empty cell
    - 1: fresh orange 
    - 2: rotten orange 
    - length of grid: [1,10]

Plan: BFS 
1. Add positions of all rotten oranges to queue and record the total number of oranges 
2. Run BFS on queue of rotten oranges until there is no more rotten oranges to add to queue 
3. If the total number of oranges == 0:
        return totalMinutes
    else: 
        return -1
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        totalOranges = 0

        queue = deque() 

        # add all rotten oranges to queue 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    totalOranges += 1

        # BFS 
        totalMinutes = 0

        while queue and totalOranges > 0: 
            # process all oranges in this moment of time 
            levelLength = len(queue)
            totalMinutes += 1

            for i in range(levelLength):
                # process current rotten orange
                r,c = queue.popleft()

                # visit neigbors to mark rotten
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c 

                    inBounds = nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0])
                    if inBounds and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 2 
                        totalOranges -= 1

        if totalOranges == 0:
            return totalMinutes

        return -1