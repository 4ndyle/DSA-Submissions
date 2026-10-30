class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r,c):
            # base case
            outOfBounds = r < 0 or r >= len(board) or c < 0 or c >= len(board[0])
            if outOfBounds or board[r][c] == 'X' or board[r][c] == 'T':
                return

            # process current node
            board[r][c] = 'T'

            # visit neighbors
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # call dfs on border
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board) - 1) or (col == 0 or col == len(board[0]) - 1):
                    dfs(row,col)

        # call dfs on non-borders 
        for row in range(len(board)):
            for col in range(len(board[0])):    
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'