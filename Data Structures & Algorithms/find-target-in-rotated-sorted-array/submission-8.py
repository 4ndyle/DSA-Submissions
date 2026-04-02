"""
Input:
    - List[int] : nums
Output:
    - int : index of the target 
Constraints:
    - runs in O(logn) time
    - unique values

Plan: Use a binary search to find the target in the rotated array

left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if num[mid] == target:
        return mid

    if num[left] < num[right], we know it is not rotated:
        perform a normal binary search
    else:
        perform the rotated binary search

return -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # find which half of the array is sorted
            if nums[left] <= nums[mid]:
                # if the target is within the sorted left half
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # if the target is within the sorted right half
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1