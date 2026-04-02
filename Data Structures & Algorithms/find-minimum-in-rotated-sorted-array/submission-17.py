"""
Input: 
    - List[int] : nums
Output:
    - int : lowest value integer in the nums list
Constraints: 
    - 1 <= nums.length <= 1000
    - -1000 <= nums[i] <= 1000

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            # when the partition is already sorted
            if nums[left] < nums[right]:
                minValue = min(minValue, nums[left])
                break

            # do binary search
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                # search the left partition for potential value less than
                minValue = min(minValue, nums[mid])
                right = mid - 1
            else:
                left = mid + 1

        return minValue

            
