"""
Input:
    - List[int] : nums
Output:
    - int : min element of the nums array

Constraints:
    - range of values: -1000 <= nums[i] <= 1000
    - 1 <= nums.length <= 1000
    - each element is unique 

Plan: 
1. O(n) - linear search to find the min value 

[6, 1, 2, 3, 4, 5]

Example:
nums = [3,4,5,6,1,2]
min = 1


left = 0
right = 5
mid = 2
3,5,2

[3,4,5,6,1,2]
currNum = 5
search right 

-----

left = 3
right = 5
mid = 4
6,1,2

[3,4,5,6,1,2]
currNum = 1
search left

-----

left = 3
right = 3
mid = 3
6,6,6

min = 1
[3,4,5,6,1,2]
currNum = 6
search left 

----

left = 2
right = 3
mid = 3

min = 1
[3,4,5,6,1,2]
currNum = 6

return nums[right]

Plan:
1. Check if the input is sorted in ascending order or rotated 
    - Comparing the value at index 0 and the last index 
        if nums[0] < nums[last index]:
            nums is sorted in ascending order, return nums[0]

2. Create a variable to keep track of the min so far 
3. Perform a binary search to find right segment of the sequence 
    - if nums[mid] > nums[right], search right
    - if nums[mid] < nums[right], search left 
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Check if the input is sorted in ascending order or rotated 
        if nums[0] <= nums[-1]:
            return nums[0]

        # Perform a binary search to find the right segment 
        left = 0
        right = len(nums) - 1
        minVal = float("inf")

        while left <= right: 
            mid = (left + right) // 2
            print(f"checking number {nums[left]}, {nums[mid]}, {nums[right]}")

            # search right partition when middle num > right number 
            if nums[mid] > nums[right]:
                print(f"searching right, left = {mid + 1}\n")
                left = mid + 1
            # search left partition when middle num > left number (nums[mid] <= right num)
            else:
                print(f"searching left, right = {mid - 1}\n")
                minVal = min(minVal, nums[mid])
                right = mid - 1

        return minVal
                
