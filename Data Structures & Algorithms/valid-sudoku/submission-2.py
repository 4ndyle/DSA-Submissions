from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = collections.defaultdict(set)
        seenCol = collections.defaultdict(set)
        seenSquare = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                currentElement = board[row][col]

                if currentElement == ".":
                    continue
                elif currentElement in seenRow[row] or currentElement in seenCol[col] or currentElement in seenSquare[(row // 3, col // 3)]:
                    return False
                else:
                    seenRow[row].add(currentElement)
                    seenCol[col].add(currentElement)
                    seenSquare[row//3, col//3].add(currentElement)

        return True
