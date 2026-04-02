class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        res_set = set()
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                if target > nums[j] + nums[k]:
                    j += 1
                elif target < nums[j] + nums[k]:
                    k -= 1
                else:
                    res_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        for r in res_set:
            res.append(list(r))

        return res