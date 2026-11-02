"""
Input:
    - list[list[str]] : board
Output:
    - None : modify the board in place
Constraints:
    - surrounded: if none of the 'O' cells are on the edge of the board
    - region: islands of 'O'
    - length of board: [1,200]
    - length of board[i]: [1,200]
    - possible values: 'O', 'X'

Plan:
1. Iterate through the borders and use a DFS search on any 'O' on the edges and change them to 
'T' to represent regions that are not surrounded
2. Go through each position on the board and change from:
    'O' -> 'X' (surrounded regions)
    'T' -> 'O' (not surrounded regions revert back)
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r,c):
            # base case: out of bounds or 'X'
            outOfBounds = r < 0 or r >= len(board) or c < 0 or c >= len(board[0])
            if outOfBounds or board[r][c] == 'X' or board[r][c] == 'T':
                return 
            
            # process the current position
            board[r][c] = 'T'

            # visit neighbors
            for dr, dc, in directions:
                dfs(r + dr, c + dc)

        # visit border
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board) - 1) or (col == 0 or col == len(board[0]) - 1):
                    dfs(row, col)

        # visit every position and update regions
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O': 
                    board[row][col] = 'X'
                elif board[row][col] == 'T': 
                    board[row][col] = 'O'