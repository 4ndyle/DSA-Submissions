"""
Input: 
    - List[int] : nums
    - int : target
Output: 
    - List[int] : [i, j] where nums[i] + nums[j] = target and i != j

nums[i] + nums[j] = target

target - nuns[i] = nums[j]
Using this, we can check to see if the other number needed to sum up to the target
is found in the array or not 

Use a dict to keep track of the values and what index they occur at 

Constraints:
    - only one valid answer exists 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dict to map each value to their index in the array
        valDict = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            # if the difference (the number we need) is already found, return i and j
            if difference in valDict:
                return [valDict[difference], i]

            # otherwise, add the current number to our valDict (value : index)
            else:
                valDict[nums[i]] = i

        

        

