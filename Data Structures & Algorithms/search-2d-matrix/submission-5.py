class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # perform a binary search on the matrix to find the row that the target is in
        left = 0
        right = m - 1

        while left <= right:
            mid = (left + right) // 2

            # if the target is in the range of the row, perform a binary search on the row to find the target
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                # perform a binary seach on the row 
                innerLeft = 0
                innerRight = n - 1

                while innerLeft <= innerRight:
                    innerMid = (innerLeft + innerRight) // 2

                    if target == matrix[mid][innerMid]:
                        return True
                    
                    if target < matrix[mid][innerMid]:
                        innerRight = innerMid - 1
                    else:
                        innerLeft = innerMid + 1

                return False

            # if the target is less than the lowest value of the row, search the left partition
            if target < matrix[mid][0]:
                right = mid - 1
            # if the target is greater than the highest value of the row, search the right partition
            else:
                left = mid + 1

        return False