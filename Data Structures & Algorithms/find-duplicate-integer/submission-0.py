class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        print(nums)

        for i in range(len(nums)):
            currentNum = nums[i]

            if currentNum == nums[i+1]:
                return currentNum

        return 0