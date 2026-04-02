"""
Input: 2D Array (representing the board)
Output: Boolean (valid sodoku board or not)
Constraints:    
    1. each row must contain 1-9 without duplicates
    2. each col must contain 1-9 without duplicates
    3. each 3x3 must contain 1-9 without duplicates

Plan:
1. Check each row in the 2D array 
2. Check each col in the 2D array
3. Check each 3x3 in the 2D array

Psuedo Code:

rows = length of the board
cols = length of a row of the board

for rowNum in range(rows):
    create a set to store numbers

    for colNum in range(cols):
        if the currentnumber at [rowNum][colNum] is between 1-9 and not in the set:
            add the number to the set
        otherwise, return False

for colNum in range(cols):
    create a set to store numbers

    for rowNum in range(rows):
        if the current element at [rowNum][colNum] is between 1-9 and not in the set:
            add the number to the set
        otherwise, it is a duplicate, simply return False
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # check each row 
        for rowNum in range(rows):
            seenNums = set()

            for colNum in range(cols):
                if board[rowNum][colNum] == ".":
                    continue
                elif board[rowNum][colNum] not in seenNums:
                    seenNums.add(board[rowNum][colNum])
                else:
                    return False

        # check each col 
        for colNum in range(cols):
            seenNums = set()

            for rowNum in range(rows):
                if board[rowNum][colNum] == ".":
                    continue
                elif board[rowNum][colNum] not in seenNums:
                    seenNums.add(board[rowNum][colNum])
                else:
                    return False

        # check each 3x3 grid
        # key: (square row, square col)
        # val: set of seen numbers
        # each square can be found using integer division
        squares = collections.defaultdict(set)

        for rowNum in range(rows):
            for colNum in range(cols):
                squareRow = rowNum // 3
                squareCol = colNum // 3
                currNum = board[rowNum][colNum]

                if currNum == ".":
                    continue
                elif currNum not in squares[(squareRow, squareCol)]:
                    squares[(squareRow, squareCol)].add(currNum)
                else:
                    return False

        return True