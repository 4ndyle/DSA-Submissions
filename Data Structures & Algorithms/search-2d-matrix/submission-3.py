"""
Input: 
    - 2D array : matrix
    - int : target
Output:
    - boolean : represent if target exists within matrix 
Constraints:    
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 100
    - -10000 <= matrix[i][j], target <= 10000

Plan: Iterate through each list and check if the target is between the first and last element values. If it is, perform
a binary search on that list to find our element. 

for row in matrix:
    if target is not in between the first and last values of row:
        continue 
    else:
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid - 1
            else:
                left  = mid + 1

        break, since no number found in list and cannot be found in others

return False
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                left = 0
                right = len(row) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if target == row[mid]:
                        return True
                    elif target < row[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1

                break
            else:
                continue

        return False
        