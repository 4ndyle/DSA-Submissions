class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i,num in enumerate(nums):
            # avoid duplicate values, excluding first element
            if i > 0 and num == nums[i-1]:
                continue

            # set up two sum to find remaining two numbers
            left = i+1
            right = len(nums) - 1

            while(left < right):
                sum = num + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([num,nums[left],nums[right]])
                    left += 1
                    # update one of the pointers to continue loop (otherwise infinite)
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result

    