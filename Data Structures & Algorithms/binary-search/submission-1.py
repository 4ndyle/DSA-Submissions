"""
Input: 
    - List[int] : nums 
    - int : target
Output: 
    - int : index of target that we are searching for 
Constraints:
    - sorted in ascending order
    - logn time complexity 
    - -10000 <= nums[i] < 10000
    - 1 <= nums.length <= 1000
    - all the integers in nums are unique 


Plan: Use a binary search to search for the target in the the nums list, splitting 
the searching partition in half each time we search. 

Psuedo Code:
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if number at middle = target:
        return middle index
    otherwise if middle number > target:
        (search the left partition)
        right = middle - 1
    otherwise the middle number < target:
        (search the right partition)
        left = mid + 1

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
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1 

            





