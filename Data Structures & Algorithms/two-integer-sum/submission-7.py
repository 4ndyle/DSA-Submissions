class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numMap:
                return [numMap[difference],i]
            else:
                numMap[nums[i]] = i

        

