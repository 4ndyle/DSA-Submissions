"""
Input:
    - List[int] : nums
    - int : target
Output:
    - List[int] : [i,j] - nums[i] + nums[j] == target
Constraints:
    - length of nums: [2,1000]
    - values of nums: [-10000000,10000000]
    - value of target: [-10000000,10000000]
    - nums[i] + nums[j] == target

Plan:
idea:
Target - Nums[i] == otherNum 

1. Create variables
    - numMap: {
        num : index
    } 
2. For i in range(len(nums))
        difference = target - num

        if difference in numsMap:
            return the index of difference and nums[i]
        else:
            add nums[i] : i to numsMap
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numMap:
                return [numMap[difference], i]
            else:
                numMap[nums[i]] = i

