
"""
Input: 
    - List[int] : nums
    - int : target
Output: 
    - List[int] : where the first and second index are the indexes of the two 
    numbers that add up to target
Constraints:
    - 2 <= nums.length <= 1000

Plan: 
1. Create a empty dict to keep track of the num : index
2. Iterate through nums
    difference = target - currNum (number that we are looking for)

    if difference exists in dict:
        return [dict[difference], currIndex]
    else:
        add the currNum to the dict with it's index
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numIndex:
                return [numIndex[difference], i]
            else:
                numIndex[nums[i]] = i 