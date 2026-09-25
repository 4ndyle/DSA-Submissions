"""
3 + 3 = 6 / 2 = 3 

4+3 = 7 / 2 = 3 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1

        return -1