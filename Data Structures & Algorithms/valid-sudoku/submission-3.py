"""
Input:
    - List[List[str]] : board 
Output: 
    - bool : whether or not the sudoku board is valid (true if valid)

1. Each row has 1-9 (no duplicates)
2. Each col has 1-9 (no duplicates)
3. Each 3x3 sub box can only have 1-9 (no duplicates)

row: 
    {
        1: {numbers in row 1}
        2: {numbers in row 2}
        3: {numbers in row 3}
        ...
    }


col: 
    {
        1: {numbers in col 1}
        2: {numbers in col 2}
        3: {numbers in col 3}
        ...
    }

how find square number:
board[0][1]
0 // 3 = 0
1 // 3 = 0

board[3][3]
3 // 3 = 1 
3 // 3 = 1

sqaure: 
    {
        (0, 0) : {numbers in square [0,0]}
    }
"""

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create a set to keep track of each row, col, and 3x3 square 
        rowNums = defaultdict(set)
        colNums = defaultdict(set)
        squareNums = defaultdict(set)

        for row in range(9):
            for col in range(9):
                currNum = board[row][col]

                if currNum == ".":
                    continue

                currSquare = (row // 3, col // 3)

                if currNum in rowNums[row] or currNum in colNums[col] or currNum in squareNums[currSquare]:
                    return False
                
                # add currNum to the col, row, and square that it's in 
                rowNums[row].add(currNum)
                colNums[col].add(currNum)
                squareNums[currSquare].add(currNum)

        print(rowNums)
        print(colNums)
        print(squareNums)

        return True







