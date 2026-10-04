"""
Input:
    -  
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minVal = float("inf")

        while left <= right:
            if nums[left] < nums[right]:
                minVal = min(minVal, nums[left])
                break

            # weird binary search
            mid = (left + right) // 2
            minVal = min(minVal, nums[mid])

            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        return minVal

