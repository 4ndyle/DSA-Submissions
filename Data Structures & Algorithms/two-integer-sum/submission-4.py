class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check if list is empty or not
        if len(nums) == 0:
            return []

        # create hashmap with num as key and index as value
        numMap = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference not in numMap:
                numMap[nums[i]] = i
            else:
                return [numMap[difference],i]

        return []

