"""
Input:
    - List[List[str]] : board
Output:
    - bool : true if board is valid, false otherwise
Constraints:
    - each row must contain digits 1-9 without duplicates
    - each col must contain digits 1-9 without duplicates
    - each of the 3x3 sub-boxes must contain 1-9 without duplicates
    - length of board: 9
    - length of board[i]: 9 
    - values of board[i]: 1-9 or '.'

Plan:
1. Create variables:
    - rows = { row # : set(numbers)}
    - cols = { col # : set(numbers)}
    - squares = { (row, col) : set(numbers)}
2. for rowNum in range(9):
        for colNum in range(9):
            val = board[rowNum][colNum]

            if val is not empty and val in board:
                return False
            otherwise:
                add val to the corresponding row, val, and square 
3. Return True is we go through whole board without duplicates
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create variables
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for rowNum in range(9):
            for colNum in range(9):
                val = board[rowNum][colNum]

                if val == '.':
                    continue
                elif val in rows[rowNum] or val in cols[colNum] or val in squares[(rowNum // 3, colNum // 3)]:
                    return False
                else:
                    rows[rowNum].add(val)
                    cols[colNum].add(val)
                    squares[(rowNum // 3, colNum // 3)].add(val)

        return True





"""
How to find square # (1-9):

row = 2
col = 1

The square would be (0,0)
row = 2 / 3 = 0 
col = 1 / 3 = 0 

row = 5
col = 0 
square = ((5 / 3), (0 / 3)) = (1, 0)

"""