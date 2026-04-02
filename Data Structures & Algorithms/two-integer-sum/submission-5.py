class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap containing difference of current number and target and its index
        numsMap = {}
        res =[]

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numsMap:
                # found other number
                res.append(min(i, numsMap[difference]))
                res.append(max(i,numsMap[difference]))
            else:   
                numsMap[nums[i]] = i

        return res
