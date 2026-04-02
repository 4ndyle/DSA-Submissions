class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference not in numMap:
                numMap[nums[i]] = i
                print(numMap)
            else:
                # print("found difference")
                return [numMap[difference],i]

        print(numMap)
        return []

