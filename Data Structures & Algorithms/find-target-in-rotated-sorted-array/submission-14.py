"""
Input:
    - List[int] : nums
    - int : target
Output:
    - int : index or -1 if not found 
Constraints:
    - O(logn) time 
    - each element is unique 
    - length: 1 <= nums.length <= 1000
    - sorted in ascending order 

Approach:
1. O(n) - Linear Search
2. O(logn) - Binary Search


Plan: Use a binary search on the rotated array with updated logic 

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    UPDATED BINARY SEARCH LOGIC
    if nums[left] > nums[right]:
        if target == nums[mid], return mid
        if target < nums[mid] and target >= nums[left], search right
        if target > nums[right], search left 

    NORMAL BINARY SEARCH LOGIC
    else:
        if target == nums[mid], return mid 
        if target < nums[mid], search left
        if target > nums[mid], search right

return -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # check which section is sorted 
            if nums[left] <= nums[mid]:
                # if the target is between the sorted range of left to mid, search left
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # if the target is between the sorted range from mid to right, search right
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # target is not found 
        return -1


"""
nums = [3,4,5,6,1,2], target = 1


Iteration 0:
left = 0
right = 5
mid = 2

nums[left] = 3
nums[mid] = 5
nums[right] = 2
[3,4,5,6,1,2]

UPDATED BINARY SEARCH LOGIC
Search right

Iteration 1:
left = 3
right = 5
mid = 4

nums[left] = 6
nums[mid] = 1
nums[right] = 2
[3,4,5,6,1,2]

return 1
"""