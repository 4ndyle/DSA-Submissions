"""
Input:
    - List[int] : nums 
    - int : target 
Output:
    - int : [i,j] such that num[i] + nums[j] == target
Constraints:
    - every input has 1 answer
    - i < j 
    - length of nums: [2,10]
    - values of nums: [-10,000,000, 10,000,000]

Example: 
[3,4,5,6]
target = 7

3 + x = 7 
4 + x = 7 
5 + x = 7
6 + x = 7

In each case, x = 7 - num[i]

check if x has occured yet, if it has, then return the index of x and current index as a pair []

Plan: 
1. Create variables 
    - numMap = {}
2. for i in range(len(nums)):
        difference = target - nums[i]

        if difference in numMap:
            return [numMap[difference], i]
        else:
            numMap[nums[i]] = i
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numMap: return [numMap[difference], i]
            
            numMap[nums[i]] = i
            