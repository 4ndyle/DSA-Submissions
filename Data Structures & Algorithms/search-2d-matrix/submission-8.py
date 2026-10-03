"""
Input:
    - List[List[int]] : matrix 
    - int: target
Output:
    - bool: true if the number is found in the mxn matrix 
Constraints:
    - O(log(m*n)) time 
    - length of m: 
    - length of n: 
    - values of matrix: 

Plan: 
1. Perform a binary search on the rows to find which 
2. Perform another binary search on the specific row to find the numeber 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        n = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2
            currList = matrix[mid]

            if target > currList[n-1]:
                left = mid + 1
            elif target < currList[0]:
                right = mid - 1
            else:
                return self.binarySearch(currList, target)

        return False

    def binarySearch(self, nums, target):
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1 
            elif target < nums[mid]:
                right = mid - 1
            else:
                return True 

        return False